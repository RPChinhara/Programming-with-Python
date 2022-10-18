from dataclasses import dataclass

@dataclass
class Job:
    job_id:str
    profit:int
    deadline:int

    def __repr__(self) -> str:
        return f"[{self.job_id}, {self.profit}, {self.deadline}]"

a = Job('1001', 150, 1)
print(a)