import streamlit as st

from core.memory import load_memory
from core.task_manager import load_tasks, add_task

from agents.ceo import CEO
from agents.cto import CTO
from agents.engineer import Engineer
from agents.marketer import Marketer
from agents.cfo import CFO

memory = load_memory()
tasks = load_tasks()

ceo = CEO()
cto = CTO()
engineer = Engineer()
marketer = Marketer()
cfo = CFO()

st.title("🚀 StartupOS")

st.header("Goal")
st.write(memory["goal"])

new_task = st.text_input("New Task")

if st.button("Add Task"):
    if new_task:
        add_task(new_task)
        st.rerun()

st.divider()

st.subheader("CEO")
st.write(ceo.think(memory, tasks))

st.subheader("CTO")
st.write(cto.think(tasks))

st.subheader("Engineer")
st.write(engineer.think())

st.subheader("Marketing")
st.write(marketer.think())

st.subheader("CFO")
st.write(cfo.think())

st.divider()

st.subheader("Tasks")

for task in tasks:
    st.write(f"- {task['task']} ({task['status']})")