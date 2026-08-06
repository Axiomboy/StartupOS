class CEO:

    def think(self, memory, tasks):

        goal = memory["goal"]

        if len(tasks) == 0:
            return "No tasks. Create a roadmap."

        return f"Our goal is: {goal}\nCurrent task: {tasks[0]['task']}"