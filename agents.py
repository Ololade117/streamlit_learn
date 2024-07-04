import streamlit as st 
symptoms = st.text_input("Enter the symptoms that you have")
medical_history = st.text_input("what is your medical history")

class agents():
    def __init__(self,role,goal,back_story,tools,verbose):

        self.role = role
        self.goal = goal
        self.back_story = back_story
        self.tools = tools
        self.verbose = verbose

    #def researcher(self):
     #   role = "Experienced Medical researcher"
      #  goal = f"Give a concise report on the following symptoms : {symptoms}, with a medical history : {medical_history}"
       # back_story = ""
        #tools = []
        #verbose = ""
        #return f"i will research on the following {symptoms} with the following {medical_history}"
    def research(symptoms, medical_history):
        return f"i will research on the following {symptoms} with the following {medical_history}"

researcher = agents(role= "Experienced Medical researcher",goal= f"Give a concise report on the following symptoms : {symptoms}, with a medical history : {medical_history}", back_story = "", tools= "" , verbose= True)
result = researcher.research(symptoms)
#st.text(result)
