import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random

# Initialize data structures
words = []
classes = []
documents = []
ignore_words = ['?', '!']

# Load intents file
data_file = open('intents.json').read()
intents = json.loads(data_file)

# Preprocess data
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenize each word in the pattern
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        # Add documents to the corpus
        documents.append((w, intent['tag']))
        # Add the tag to our classes list if not already present
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize, lower each word, and remove duplicates
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# Sort classes
classes = sorted(list(set(classes)))

# Print basic information
print(f"{len(documents)} documents")
print(f"{len(classes)} classes: {classes}")
print(f"{len(words)} unique lemmatized words: {words}")

# Save the words and classes
pickle.dump(words, open('texts.pkl', 'wb'))
pickle.dump(classes, open('labels.pkl', 'wb'))

# Create training data
training = []
output_empty = [0] * len(classes)

for doc in documents:
    # Initialize bag of words
    bag = []
    pattern_words = doc[0]
    # Lemmatize each word and lower it
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    # Create bag of words array with 1 if word match found in current pattern
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    
    # Output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    
    training.append([bag, output_row])

# Shuffle features and labels separately
random.shuffle(training)

# Separate features and labels
train_x = np.array([elem[0] for elem in training])
train_y = np.array([elem[1] for elem in training])

print("Training data created")

# Create model - 3 layers
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile model
# Update SGD optimizer
sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)

# Compile model with the updated optimizer
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Fit and save the model
hist = model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)
model.save('model.h5', hist)

print("Model created and saved")
