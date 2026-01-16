# =========================================

# Student Name: Oluwole Amos

# Learner ID: ALT/SOD/TIN/025/0061

# Track: Data Engineering

# Mini Project: Contact Tracing System

# =========================================

infection_status = {}
contacts = []

def add_person(name: str, infected:bool):
  name = name.strip() #remove extra spaces)
  if name in infection_status:#check if person exists
    infection_status[name] = infected 
  else:
    infection_status[name] = infected

def add_contact(person1: str, person2: str, duration: int):
  if duration < 1:
    raise ValueError('Duration must be greater than zero')
  if person1 == person2:
    raise ValueError("Person 1 and Person 2 cannot be the same")
  
  if person1 not in infection_status:
    add_person(person1, False)
  
  
  if person2 not in infection_status:
    add_person(person2, False)
  
  contacts.append((person1, person2, duration))

def  get_high_risk_contacts() -> list:
  exposure_map = {}  

  for p1, p2, duration in contacts:
      p1_infected = infection_status.get(p1, False)
      p2_infected = infection_status.get(p2, False)

      # Only consider exposure involving infected people
      if p1_infected and not p2_infected:
          key = (p2, p1)
      elif p2_infected and not p1_infected:
          key = (p1, p2)
      else:
          continue

      exposure_map[key] = exposure_map.get(key, 0) + duration
  high_risk_contacts = []
  for (exposed, infected), total in exposure_map.items():
    if total >= 15:
      high_risk_contacts.append((exposed, infected, total))
        
  high_risk_contacts = sorted(high_risk_contacts, key=lambda x: x[2], reverse=True)
  return high_risk_contacts



def print_report():
  high_risk_data = get_high_risk_contacts()
  print("Exposure Report")
  print("---------")
  print("Total People: ", len(infection_status))
  print("Total contact events: ", len(contacts))
  print("Infected People: ", len([candidate for candidate in infection_status if infection_status[candidate] == True]))
  print("High Risk Individuals:  ", len(high_risk_data))
  print("Top exposures:")
  for exposed, infected, duration in high_risk_data:
    print(f"{exposed} was exposed to {infected} for {duration} minutes")
  


add_person("Dapo", False)
add_person("Jack", True)
add_person("Mike", True)

add_contact("Dapo", "Jack", 2)
add_contact("Anu", "Jack", 15)
add_contact("Dapo", "Jack", 14)

print("infection status:::::::::")
print(infection_status)
print("contacts::::::::")
print(contacts)


print_report()
