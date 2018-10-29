#Defines a dependency between objects so that whenever an object changes its state, all its dependents are notified.

#A good example would be the job seekers where they subscribe to some job posting site and they are notified whenever there is a matching job opportunity.


class JobnPost:

    def __init__(self, title):
        self.name = name

    def get_title(self):
        return self.title

class JobSeeker:

    def __init__(self, name):
        self.name = name

    def on_job_post(self, job):
        print('Ola {}! Nova vaga postada: {}'.format(self.name, job.title))

class JobPostings:

    def __init__(self):
        self.observers = list()

    def notify(self, job_posting):
        for observer in self.observers:
            observer.on_job_post(job_posting)

    def attach(self, observer):
        self.observers.append(observer)

    def add_job(self, job_posting):
        self.notify(job_posting)

if __name__ == '__main__':

    #Cria Subscribers
    john_doe = JobSeeker('John Doe')
    jane_doe = JobSeeker('Jane Doe')
    kane_doe = JobSeeker('Kane Doe')

    #Cria publisher e o atrela a subscribers
    job_posting = JobPostings()
    job_posting.attach(john_doe)
    job_posting.attach(jane_doe)

    # adiciona um novo trabalho e ve se o subscribers foi notificado
    job_posting.add_job(JobPost('Engenheiro de Software'))

    # output:
    # Ola John Doe! Nova vaga postado: Engenheiro de Software
    # Ola Jane Doe! Nova vaga postado: Engenheiro de Software
