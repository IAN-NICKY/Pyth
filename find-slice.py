text = "X-DSPAM-Confidence:    0.8475"

#checking for position of colon
colpos = text.find(':') 


extract = text[colpos+1:]#starting from position next to poosition of colon
extract= float(extract) #converting string to float to remove extra space

print(extract)


