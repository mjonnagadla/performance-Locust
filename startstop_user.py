#User, TaskSet and SequentialTaskset contains on_stat() and on_stop() methods
#on_start() will be called once the execution starts
#on_stop() will be called once the execution time is lapsed
#no need to decarate these methods with @task
#These two methods will run only one time in total execution
#These methods will run for user once in TaskSet and SequentialTaskset classes

from locust import User, task, constant;

class myUser(User):
    wait_time=constant(1)

    def on_start(self):
        print("Start Execution")

    @task
    def login(self):
        print('My Test executed')
    
    @task
    def user2(self):
        print("Task 2")

    def on_stop(self):
        print("Stop Execution")

