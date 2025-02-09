#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from openai import *
import os 



#Base message

#Main body of the message


class ChatGPT_methods:
    def __init__(self):
              
        self.client = OpenAI(
            #!Delete before pushing to the repository
            api_key= ""#Enter you API key here or read from ini/env file
        )
        self._module = "gpt-4o-mini"
        self.message = None
        
        

    
        
    def get_response(func):
        def wrapper(self,*args,**kwargs):
            func(self,*args,**kwargs)
            print(self.message)
            try:
                completion = self.client.chat.completions.create(
                    model=self._module,
                    store=True,
                    messages=[
                        {"role": "user", "content": self.message}
                    ]
                )
                return completion.choices[0].message.content  
            except Exception as e:
                return None
        return wrapper
        

   
    def Refill_topic(self):
        try:
            with open("Topics_list.txt","r+") as file:   
                file.seek(0)# Ensure that the pointer is at the beginning of the file
                lines = file.readlines()
                if lines:
                    return None
                
                self.message = ""#!Enter generral suject here
                #new_topics  = self.wrapper(func,)
                
                
                currect_topic = lines[0].strip()#Remove the '\n' from the string and save the topic into the variable
                file.seek(0)#Return the pointer to the beginning of the file
                file.truncate()#Clear the file
                # Write all the topics again except the first one
                file.writelines(lines[1:])    
            return currect_topic
        except Exception as e:
            return
   
   
    
    @staticmethod
    def _change_topic():
        try:
            if not os.path.exists("Topics_list.txt"):
                return None#TODO - topic.txt will be updated with the user's input
            with open("Topics_list.txt","r+") as file:   
                file.seek(0)# Ensure that the pointer is at the beginning of the file
                lines = file.readlines()
                if not lines:
                    return None
                currect_topic = lines[0].strip()#Remove the '\n' from the string and save the topic into the variable
                file.seek(0)#Return the pointer to the beginning of the file
                file.truncate()#Clear the file
                # Write all the topics again except the first one
                file.writelines(lines[1:])    
            return currect_topic
        except Exception as e:
            return None
        
    
        
        
        
