import utils

print('New Model Update:')



question = "What should I do if my Apple Watch won’t connect to my iPhone?"
print("Input Question is: ", question)
answer = utils.getResponse(question)
print(answer)

question = "Could you please provide the list of Products that are available in stock ?"
print("Input Question is: ", question)
answer = utils.getResponse(question)
print(answer)


question = "Could you tell me order number 89086"
print("Input Question is: ", question)
answer = utils.getResponse(question)
print(answer)



question = "Could you please provide the Price for Wireless Headphones ?"
print("Input Question is: ", question)
answer = utils.getResponse(question)
print(answer)


"""

question = "Could you please provide the Order status for order number 89086 ?"
print("Input Question is: ", question)
answer = utils.query_slm(question)
print(answer)


question = "I would like to give feedback"
print("Input Question is: ", question)
answer = utils.query_slm(question)
print(answer)

question = "Would you like to give feedback ? Yes"
print("Input Question is: ", question)
answer = utils.query_slm(question)
print(answer)


print('LLM Model for Text to DB Search & Response in Natural Language is as below:')

question = "Could you please provide the list of Products that are available in stock ?"
print("Input Question is: ", question)
answer = utils.query_llm(question)
print(answer)


question = "Could you please provide the Order status for order number 89086"
print("Input Question is: ", question)
answer = utils.query_llm(question)
print(answer)

question = "What is the Price for Product Car Vacuum Cleaner ?"
print("Input Question is: ", question)
answer = utils.query_llm(question)
print(answer)


question = "Could you please provide the Order status for order number 1234"
print("Input Question is: ", question)
answer = utils.query_llm(question)
print(answer)

"""