import re

class Stack:
     def __init__(self):
         self.file = input("File: ")
         self.tags = []
         self.tags_f = []
         self.tags_tabs_f = []
         self.tabs = []
         self.tmp = []

     def list_of_tags(self):
         print("List of whitespaces with \",\": ")
         tags_str = input()
         for el in tags_str.split(","):
             self.tags.append(el)
         return None

     def treatment(self):
         try:
             file = open(self.file, 'r')
         except():
             print("Incorrect file path. Program stopped.")
         for line in file:
             for el in self.tag_list:
                self.whitespace_tag_list_in_file.append(re.findall(" *" + el, line))
                self.tmp_list.append(re.findall(el, line))
                for element in self.tmp_list:
                    if len(element) < 1:
                        self.tmp_list.remove(el)
                for el in self.whitespace_tag_list_in_file:
                    if len(el) < 1:
                        self.whitespace_tag_list_in_file.remove(el)
         for el in self.tmp:
             self.tags_f.append(el[0])
         self.tmp[:] = []
         file.close()
         x = 0
         for el in self.tags_tabs_f:
             self.tags_tabs_f[x] = el[0]
             x = x + 1

         file = open('html.txt', 'r')
         res_file = open("html_result.txt", "w")
         for element in self.tags_f:
             self.tmp.append("<"+element+">")
         schet = 0
         for line in file:
             res_file.write(line.replace(self.tags_f[schet], self.tmp[schet]))
             if schet < len(self.tmp)-1:
                 schet = schet + 1
         res_file.close()
         self.tmp[:] = []
         file.close()
         res_file.close()

         for el in self.tags_tabs_f:
             self.tmp.append(re.findall(" *", el))
         for el in self.tmp:
            self.tabs.append(el[0])
         self.tmp[:] = []

         res_file = open("html_result.txt", "a")
         x = 0
         for el in self.tags_f[::-1]:
             self.tmp.append(el)
         for el in self.tabs[::-1]:
             res_file.write(el + "</"+str(self.tmp[x]) + ">\n")
             x = x + 1
         res_file.close()
         print("All done")
         return None