question = ""
choices =  ""
expected = "" 



questions = [
    {
      "question": "What is the capital of Chile?",
      "choices": [ "Santiago", "Berlin"], 
      "expected": "Santiago" # <---- use this to govern if the input is correct or not.
    }, 
    {
    "question": "What is the highest mountain in Britain?",
    "choices": [ "Ben Nevis", "Ben Wevis"],
    "expected": "Ben Nevis"
   },
  {
    "question": " What is the smallest country in the world?",
    "choices": [ "Vatican City", "China"],
    "expected": "Vatican City"
   },
   {
    "question": "Alberta is a province of which country?",
    "choices": [ "Canada", "Italy"],
    "expected": "Canada"
   },
   {
    "question": "How many countries still have the shilling as currency?",
    "choices": [ "Kenya", "Uk"],
    "expected": "Kenya"
   },
   {
    "question": "Which is the only vowel not used as the first letter in a US State?",
    "choices": [ "E", "U"],
    "expected": "E"
   },
   {
    "question": "What is the largest country in the world?",
    "choices": [ "Russia", "Germany"],
    "expected": "Russia"
   },
   {
    "question": "Where would you find the River Thames?",
    "choices": [ "London", "Scotland"],
    "expected": "London"
   },
   {
    "question": "What is the hottest continent on Earth?",
    "choices": [ "Africa", "Netherlands"],
    "expected": "Africa"
   },
   # this is an object and is also an item in the list
   {
    "question": "What is the longest river in the world?",
    "choices": [ "River Nile", "Ur Maw"],
    "expected": "River Nile"
   }    
]

# recursive furunction
def prompt_for_response(index_of_question=0, retries=0):
  index = index_of_question
  # Get a specific item by index from the list called questions. 
  # Than, use the key "questions" to get the question as a value. 
  question = questions[index]["question"]
  # choices = questions[index]["choices"]
  expected = questions[index]["expected"]

  # Prompt user for input...
  # Variable we stored response in ;) 
  response = input(question)

  # Store input in object
  questions[index]["response"] = response 

  # Check if the response is contained in the list of choices.
  # https://thispointer.com/python-how-to-check-if-an-item-exists-in-list-search-by-value-or-condition/ 
  
  # if response in choices:
  #   print("Invalid Response")
  # does the response match the expected response ..
  if response.lower() == expected.lower():    
    print("Correct")
  else:
    print("Incorrect")
    # I am recursive because i call myself
    if retries >= 5:
      print("You`ve retried too many times...")
    else: 
      return prompt_for_response(index, retries + 1)


# len -> length
# len(questions) #=> length of questions, how many items are in the list. 

# range
# range(len(questions)) # => 0,1,2,3,.... length of questions.
 
# Gathering the length of the list called questions to store it in a variable called number_of_questions
number_of_questions = len(questions)

# This is a loop, you are looping over each question
for index in range(number_of_questions):
  prompt_for_response(index)


