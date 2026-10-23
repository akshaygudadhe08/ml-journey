x = 5
y = 3.14
name = "John Singha"
flag = True
nothing = None

print("Day 2 : Data Types in Python")
print(type(x))
print(type(y))
print(type(name))
print(type(flag))
print(type(nothing))

priority = "4"
wordCount = "150"
has_Attachment = True

print(f"Ticket Priority : {priority}, words : {wordCount}, Double Words : {wordCount * 2}")

text = " ERROR: Login failed for user@example.com "
print(text.strip())
print(text.lower())
print(text.upper())
print(text.split(":"))
print(text.replace("ERROR", "WARN"))
print(text.startswith(" ERROR"))
print(text.endswith(" "))
print("user@example.com" in text)

print("Severity ->" + text.split(":")[0].strip())
print("Action ->" + text.split(":")[1].split("for")[0].strip())
print("Email ->" + text.split("for")[1].strip())


#Exercise 2
print(f"Ticket Priority : {priority}, words : {wordCount}, has Attachment : {has_Attachment}")

#Exercise 3
raw = " BILLING issue: refund not processed "

print(raw.strip().upper())
print(len(raw.strip().split(" ")))
print(raw.strip().startswith("BILLING"))