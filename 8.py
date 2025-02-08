def helper(work):
    work_in_memory = work

    def helper(work):
        return f"I will hwlp you with your {work_in_memory}. Afterwards I will help you with {work}"
    return helper


helper = helper("homework")
print(helper("clearning"))
print(helper("driving"))
