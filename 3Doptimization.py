from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int

def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Оптимізує чергу 3D-друку згідно з пріоритетами та обмеженнями принтера

    Args:
        print_jobs: Список завдань на друк
        constraints: Обмеження принтера

    Returns:
        Dict з порядком друку та загальним часом
    """
    printer = PrinterConstraints(
        max_volume=constraints["max_volume"],
        max_items=constraints["max_items"]

    )
    if printer.max_items <= 0 or printer.max_volume <= 0:
        return {
            "print_order": [],
            "total_time": 0
        }
    jobs = []
    for job in print_jobs:
        if job["volume"] <= printer.max_volume:
            jobs.append(PrintJob(
                id=job["id"],
                volume=job["volume"],
                priority=job["priority"],
                print_time=job["print_time"]
            ))
    #sort jobs by priority (descending) and then by print time (ascending)
    jobs.sort(key=lambda x: (x.priority, -x.volume))
    print_order = []
    total_time = 0

    while jobs:
        current_group: List[PrintJob] = []
        current_volume = 0.0

        i=0
        while i < len(jobs):
            job = jobs[i]
            if (len(current_group) < printer.max_items and
            current_volume + job.volume <= printer.max_volume):
                current_group.append(job)
                current_volume += job.volume
                print_order.append(job.id)
                jobs.pop(i)  # Remove the job from the list
            else:
                i += 1  # Move to the next job
        if current_group:
            group_time = max(job.print_time for job in current_group)
            total_time += group_time
        else:
            break  # No more jobs can be added, exit the loop
            

    return {
        "print_order": print_order,
        "total_time": total_time
    }

# Тестування
def test_printing_optimization():
    # Тест 1: Моделі однакового пріоритету
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    # Тест 2: Моделі різних пріоритетів
    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},  # лабораторна
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},  # дипломна
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}  # особистий проєкт
    ]

    # Тест 3: Перевищення обмежень об'єму
    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("Тест 1 (однаковий пріоритет):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Порядок друку: {result1['print_order']}")
    print(f"Загальний час: {result1['total_time']} хвилин")

    print("\\nТест 2 (різні пріоритети):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Порядок друку: {result2['print_order']}")
    print(f"Загальний час: {result2['total_time']} хвилин")

    print("\\nТест 3 (перевищення обмежень):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Порядок друку: {result3['print_order']}")
    print(f"Загальний час: {result3['total_time']} хвилин")

if __name__ == "__main__":
    test_printing_optimization()

