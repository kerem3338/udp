#Universel Document Page
import json
import os
import sys
from tkinter import *


class Executer:
	def __init__(self, file):
		#Tkinter
		self.root = Tk()
		self.root.title("Udp Service")
		self.root.geometry("500x500")
		
		self.content=Label(self.root)
		self.content.pack()
		
		self.file=False
		self.json=False
		if os.path.isfile(file):
			self.file=file

			file_content=open(file, "r", encoding="utf8")
			self.json = json.load(file_content)
			self.execute()
		else:
			self.file=None
			print("Error: File Not Found")
		
		
		
	def execute(self):
		if "title" in self.json:
			self.root.title(self.json["title"])
		if "udp_geometry" in self.json:
			self.root.geometry(self.json["udp_geometry"])
		if "content" in self.json:
			if "align" in self.json["content"]:
				if self.json["content"]["align"] == "left":
					self.content.pack(side=LEFT)
				elif self.json["content"]["align"] == "right":
					self.content.pack(side=RIGHT)
				elif self.json["content"]["align"] == "top":
					self.content.pack(side=TOP)
				elif self.json["content"]["align"] == "bottom":
					self.content.pack(side=BOTTOM)
				else:
					print("Error: align not found")
			try:
				self.content["text"]=text=self.json["content"]["text"]
			except TypeError:
				self.content.config(text=self.json["content"])
		self.root.mainloop()
		


