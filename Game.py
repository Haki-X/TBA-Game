import time
import sys
import random
from datetime import datetime, timedelta


class Character:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.mood = 50
        self.courage = 0
        self.intelligence = 0
        self.social = 0
        self.career_progress = 0
        self.money = 100  
        self.health = 100 
        self.mental_health = 100 # 
        self.relationship_status = {} 
        self.future_memories = []
        self.ending = ""

    def display_status(self):
        print("\n--- Character Status ---")
        print(f"Name: {self.name}")
        print(f"Energy: {self.energy}/100")
        print(f"Mood: {self.mood}/100")
        print(f"Health: {self.health}/100") 
        print(f"Mental Health: {self.mental_health}/100") 
        print(f"Money: ${self.money}") 
        print(f"Courage: {self.courage}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Social: {self.social}")
        print(f"Career Progress: {self.career_progress}")
        print("--- Relationships ---") 
        if not self.relationship_status:
            print("No significant relationships yet.")
        else:
            for person, data in self.relationship_status.items():
                print(f"- {person}: {data['status']} (Level: {data['level']})")
        print("-----------------------")

    def change_energy(self, amount):
        self.energy += amount
        if self.energy > 100: self.energy = 100
        elif self.energy < 0: self.energy = 0

    def change_mood(self, amount):
        self.mood += amount
        if self.mood > 100: self.mood = 100
        elif self.mood < 0: self.mood = 0

    def change_money(self, amount):
        self.money += amount
        if self.money < 0: self.money = 0 

    def change_health(self, amount): 
        self.health += amount
        if self.health > 100: self.health = 100
        elif self.health < 0: self.health = 0

    def change_mental_health(self, amount):
        self.mental_health += amount
        if self.mental_health > 100: self.mental_health = 100
        elif self.mental_health < 0: self.mental_health = 0

    def add_courage(self, amount):
        self.courage += amount

    def add_intelligence(self, amount):
        self.intelligence += amount

    def add_social(self, amount):
        self.social += amount

    def add_career_progress(self, amount):
        self.career_progress += amount

    def update_relationship(self, person_name, status, level_change=0): 
        if person_name not in self.relationship_status:
            self.relationship_status[person_name] = {'status': status, 'level': 0}
        
        self.relationship_status[person_name]['status'] = status
        self.relationship_status[person_name]['level'] += level_change
        
        if self.relationship_status[person_name]['level'] > 100:
            self.relationship_status[person_name]['level'] = 100
        elif self.relationship_status[person_name]['level'] < 0:
            self.relationship_status[person_name]['level'] = 0


    def add_memory(self, memory):
        self.future_memories.append(memory)

class Scene:
    def __init__(self, title, narration, choices):
        self.title = title
        self.narration = narration
        self.choices = choices

    def display(self, current_date): 
        clear_screen()
        print_divider()
        print(f"\nDate: {current_date.strftime('%Y-%m-%d')}\n") 
        print(f"## {self.title}\n")
        slow_type(self.narration)
        print("\n")
        for i, (choice_text, _) in self.choices.items():
            print(f"[{i}] {choice_text}")
        print_divider()

    def make_choice(self, user_choice, character, current_date): 
        if user_choice in self.choices:
            _, effect_function = self.choices[user_choice]
            effect_function(character)
            return True, current_date + timedelta(days=random.randint(7, 30))
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)
            return False, current_date


def slow_type(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_divider(length=50):
    print("=" * length)

def clear_screen():
    print("\n" * 50)

def intro_game():
    print_divider()
    slow_type("Welcome to 'Life's Replay'")
    print_divider()
    slow_type("A text-based adventure about second chances...")
    time.sleep(2)
    clear_screen()

current_game_date = datetime(2005, 7, 1) 



#Prologue
def accept_fate(character):
    slow_type("You decide to accept reality. The death you feel now is no different from your old life. Emptiness extends its hand, and you accept your fate without a second thought.")
    character.ending = "Fate Accepted"

def return_to_past(character):
    slow_type("Though bitter, there's a glimmer of hope in your heart. A chance to change everything. You step forward into the light.")
    character.ending = "Past Begins"

# 10th Grade
def confront_bullies(character):
    slow_type("You take a deep breath. For the first time, you fight back. Your courage surprises them, and they back down. Some students are secretly impressed.")
    character.add_courage(10)
    character.add_social(5)
    character.change_mood(10)
    character.add_memory("Confronted bullies in 10th grade.")
    print(f"Courage +10, Social +5, Mood +10") 

def ignore_bullies(character):
    slow_type("As usual, you look down, letting the taunts pass. The pain is familiar, but you feel a little emptier.")
    character.change_mood(-5)
    character.change_mental_health(-10) 
    character.add_memory("Ignored bullies in 10th grade.")
    print(f"Mood -5, Mental Health -10") 

def invite_friends_to_study(character):
    slow_type("Awkwardly, you invite some classmates to study together. It's stiff at first, but slowly the conversation flows. You feel a little more connected.")
    character.add_social(10)
    character.add_intelligence(5)
    character.change_mood(10)
    character.update_relationship("Budi", "Friend", 15) 
    character.update_relationship("Sita", "Acquaintance", 5) 
    character.add_memory("Started friendships in 10th grade.")
    print(f"Social +10, Intelligence +5, Mood +10. Budi Relationship +15, Sita Relationship +5.") # Feedback

def focus_on_studying_alone(character):
    slow_type("You choose to study alone in the library, lost in books. Your knowledge grows, but the loneliness feels more real.")
    character.add_intelligence(10)
    character.change_mood(-5)
    character.add_social(-2) 
    character.add_memory("Studied alone in 10th grade.")
    print(f"Intelligence +10, Mood -5, Social -2") 

def do_part_time_job_hs(character): 
    slow_type("You found a part-time job at a local cafe. It's tiring but you earn some money and learn about responsibility.")
    character.change_money(50)
    character.change_energy(-15)
    character.change_mood(5)
    character.add_memory("Worked a part-time job in high school.")
    print(f"Money +$50, Energy -15, Mood +5")

def relax_at_home_hs(character): 
    slow_type("You decide to just relax at home. You catch up on sleep and your favorite shows.")
    character.change_energy(20)
    character.change_mood(10)
    character.change_mental_health(5)
    print(f"Energy +20, Mood +10, Mental Health +5")

# 11th Grade
def pursue_dream_career(character):
    slow_type("You decide to focus entirely on subjects that support your career dreams. Every book and every project is an investment in the future. You feel enthusiastic.")
    character.add_intelligence(15)
    character.add_career_progress(20)
    character.change_mood(15)
    character.change_mental_health(5)
    character.add_memory("Focused on career in 11th grade.")
    print(f"Intelligence +15, Career Progress +20, Mood +15, Mental Health +5") 

def pursue_school_crush(character):
    slow_type("You spend time thinking about and trying to approach 'them'. There are happy moments, but more often disappointment and insecurity.")
    character.change_mood(-10)
    character.change_energy(-10)
    character.change_mental_health(-15) 
    
    
    if character.social < 20:
        character.update_relationship("Maya", "Unrequited Love", -10)
        slow_type("Your attempts were awkward and didn't go anywhere. Maya seems to avoid you now.")
    else:
        character.update_relationship("Maya", "Brief Dating", 20)
        slow_type("You manage to get her attention, and you briefly date. It's an emotional roller coaster.")
    
    character.add_memory("Pursued a crush in 11th grade.")
    print(f"Mood -10, Energy -10, Mental Health -15") 

# 12th Grade
def join_competition(character):
    slow_type("You sign up for a science competition/olympiad. The process is challenging, but you learn a lot and gain recognition.")
    character.add_intelligence(20)
    character.add_career_progress(25)
    character.change_mood(20)
    character.change_energy(-15) 
    character.add_memory("Participated in a competition in 12th grade.")
    print(f"Intelligence +20, Career Progress +25, Mood +20, Energy -15") 

def decline_competition(character):
    slow_type("You feel unprepared and miss the competition opportunity. There's a slight regret, but you avoid the pressure.")
    character.change_mood(-5)
    character.change_mental_health(5) 
    character.add_memory("Declined a competition in 12th grade.")
    print(f"Mood -5, Mental Health +5") 

def be_active_in_organization(character):
    slow_type("You join the student council/organization. You learn to lead, collaborate, and interact with many people. Your social network expands.")
    character.add_social(20)
    character.add_courage(10)
    character.change_mood(15)
    character.change_energy(-10) 
    character.update_relationship("Organization Team", "Active Member", 30)
    character.add_memory("Active in an organization in 12th grade.")
    print(f"Social +20, Courage +10, Mood +15, Energy -10. Organization Team Relationship +30") # Feedback

def not_active_in_organization(character):
    slow_type("You choose to stay focused on personal studies and avoid organizational activities. You have more free time, but less social interaction.")
    character.change_mood(-5)
    character.add_memory("Not active in an organization in 12th grade.")
    print(f"Mood -5") 

# College/Early Career 
def take_internship(character):
    slow_type("You proactively seek internship experience at your dream company. It's hard work, but the door to your career opens wider.")
    character.add_career_progress(30)
    character.add_social(10)
    character.change_energy(-10)
    character.change_mental_health(-5) 
    character.change_money(100) 
    character.add_memory("Interned in early career.")
    print(f"Career Progress +30, Social +10, Energy -10, Mental Health -5, Money +$100") # Feedback

def focus_on_academics(character):
    slow_type("You decide to focus entirely on academic grades. Your GPA is brilliant, but you lack practical experience.")
    character.add_intelligence(15)
    character.change_energy(-5)
    character.change_mood(5) 
    character.add_memory("Focused on academics in early career.")
    print(f"Intelligence +15, Energy -5, Mood +5") 

def enter_serious_relationship(character):
    slow_type("You meet someone special and decide to build a serious relationship. This brings happiness and new challenges.")
    character.update_relationship("Partner", "Serious", 50)
    character.change_mood(25)
    character.add_social(15)
    character.change_energy(-5) 
    character.add_memory("Built a serious relationship.")
    print(f"Mood +25, Social +15, Energy -5. Partner Relationship +50") 

def focus_on_self(character):
    slow_type("You choose to stay single and focus on self-development. This gives you freedom, but sometimes it feels lonely.")
    character.change_mood(-5)
    character.change_mental_health(5)
    character.add_memory("Focused on self in early career.")
    print(f"Mood -5, Mental Health +5")

def pursue_hobby(character):
    slow_type("You pick up a new hobby, like painting or playing an instrument. It's a great way to unwind and express yourself.")
    character.change_mood(15)
    character.change_mental_health(10)
    character.change_money(-20) 
    character.add_memory("Pursued a new hobby.")
    print(f"Mood +15, Mental Health +10, Money -$20")

# Mid-Career 
def take_business_risk(character):
    slow_type("You make a brave decision to start your own business or take on a high-risk project. It's very challenging, but the potential rewards are huge.")
    character.add_courage(20)
    character.add_career_progress(40)
    character.change_energy(-20)
    character.change_money(-200) 
    character.change_mental_health(-20) 
    
    if character.career_progress >= 50 and character.intelligence >= 60:
        slow_type("Your decision paid off! Your business grew rapidly or your project was a huge success!")
        character.change_mood(30)
        character.change_money(500)
        character.add_career_progress(50)
    else:
        slow_type("Unfortunately, the risk was too great without a strong foundation. Your business struggled.") # Corrected "Sayangnya"
        character.career_progress -= 10
        character.change_mood(-20)
        character.change_money(-100) 
        character.change_mental_health(-10)
    character.add_memory("Took business risk in mid-career.")
    print(f"Courage +20, Career Progress +40, Energy -20, Money -$200, Mental Health -20") # Base feedback

def stabilize_in_job(character):
    slow_type("You choose to stay stable in your current job, focusing on promotions and comfort. Growth might be slow, but safe.")
    character.add_career_progress(15)
    character.change_mood(5)
    character.change_money(150) 
    character.change_mental_health(10) 
    character.add_memory("Stabilized in job in mid-career.")
    print(f"Career Progress +15, Mood +5, Money +$150, Mental Health +10") 

def make_friends(character):
    slow_type("You proactively make and maintain new friendships. You find support and happiness in a strong social circle.")
    character.add_social(25)
    character.change_mood(20)
    character.update_relationship("New Friends", "Close", 40)
    character.add_memory("Made friends in mid-career.")
    print(f"Social +25, Mood +20. New Friends Relationship +40") 

def live_independently(character):
    slow_type("You feel comfortable with independence and don't seek much new social interaction. Life feels calm, but sometimes loneliness creeps in.")
    character.change_mood(-10)
    character.change_mental_health(-5) 
    character.add_memory("Lived independently in mid-career.")
    print(f"Mood -10, Mental Health -5") 

#Health-related options
def exercise(character):
    slow_type("You commit to a regular exercise routine. Your body feels stronger, and your mind clearer.")
    character.change_health(15)
    character.change_energy(10)
    character.change_mood(10)
    character.change_money(-10)
    print(f"Health +15, Energy +10, Mood +10, Money -$10")

def neglect_health(character):
    slow_type("You prioritize other things over your physical well-being. You often feel tired and sluggish.")
    character.change_health(-10)
    character.change_energy(-5)
    character.change_mood(-5)
    print(f"Health -10, Energy -5, Mood -5")

#  Random Events
def trigger_random_event(character):
    events = [
        ("Unexpected Bonus!", "Your company announced an unexpected bonus!", lambda c: (c.change_money(100), c.change_mood(10), slow_type("Money +$100, Mood +10"))),
        ("Minor Sickness", "You caught a minor cold. You feel a bit under the weather.", lambda c: (c.change_health(-10), c.change_energy(-10), c.change_mood(-5), slow_type("Health -10, Energy -10, Mood -5"))),
        ("Old Friend Reconnects", "An old friend from school reaches out! You have a nice chat.", lambda c: (c.add_social(5), c.change_mood(5), c.update_relationship("Old Friend", "Reconnected", 10), slow_type("Social +5, Mood +5, Old Friend Relationship +10"))),
        ("Public Speaking Opportunity", "You're asked to give a presentation. It's nerve-wracking!", lambda c: (c.add_courage(5) if c.courage < 30 else c.change_mental_health(-5), c.change_mood(5) if c.courage >= 30 else c.change_mood(-10), slow_type("Courage +5 (if low) or Mental Health -5 (if high), Mood change based on courage"))),
        ("Financial Setback", "An unexpected bill or expense hits your wallet.", lambda c: (c.change_money(-75), c.change_mood(-10), slow_type("Money -$75, Mood -10"))),
        ("Inspiring Book/Movie", "You stumbled upon a truly inspiring book or movie that brightens your perspective.", lambda c: (c.change_mental_health(10), c.change_mood(5), slow_type("Mental Health +10, Mood +5"))),
    ]

    if random.random() < 0.25: 
        event_name, event_narration, event_effect = random.choice(events)
        print_divider()
        slow_type(f"\n--- RANDOM EVENT: {event_name} ---")
        slow_type(event_narration)
        event_effect(character)
        time.sleep(2)
        print_divider()

# --- Main Game Loop ---
def main_game():
    global current_game_date
    intro_game()
    player_name = input("What's your name? ")
    player = Character(player_name)

    # Prologue
    prologue_scene = Scene(
        "The Last Moment...",
        "The world spins, pain spreads through your body. Ambulance lights flash, sirens wail in the distance. You lie there, gasping for breath. Your 35 years of life, empty and alone, flash before your eyes. Suddenly, a bright light appears, accompanied by a calming voice:\n'Tired soul, you have arrived at the crossroads of destiny. You can accept this end and step with Me into the next realm, or return. Return and change all the choices that led you to this emptiness. The choice is yours.'",
        {
            1: ("Accept Fate and step into the Light.", accept_fate),
            2: ("I want to go back. Give me a chance to change everything!", return_to_past)
        }
    )

    while True:
        prologue_scene.display(current_game_date)
        choice = input("Your choice: ")
        if choice.isdigit():
            success, current_game_date = prologue_scene.make_choice(int(choice), player, current_game_date)
            if success:
                break
        else:
            print("Invalid input. Please enter a number.")
            time.sleep(1)

    if player.ending == "Fate Accepted":
        slow_type("\nGame over. May your journey find peace.")
        return

    slow_type("\n--- Second Chance Begins! ---")
    slow_type(f"You feel a jolt of energy, and suddenly, the world spins. A rush of sounds fills your ears. The smell of chalk and old books hits you. You open your eyes... You're in a classroom. A gray and white uniform. It's {current_game_date.year}, your 10th grade year.")
    time.sleep(3)
    player.display_status()

    # Adegan Kelas 10
    current_game_date = datetime(2005, 9, 1) 
    adegan_kelas10_intro = Scene(
        "Back to 10th Grade: The Bully Incident",
        "The recess bell rings, and a group of popular boys start teasing a student reading in the corner, just like always. You remember, you used to just keep your head down. Now, what will you do?",
        {
            1: ("Bravely confront the bullies and defend the student.", confront_bullies),
            2: ("Stay silent and let them be, like you used to.", ignore_bullies)
        }
    )
    while True:
        adegan_kelas10_intro.display(current_game_date)
        choice = input("Your choice: ")
        if choice.isdigit():
            success, current_game_date = adegan_kelas10_intro.make_choice(int(choice), player, current_game_date)
            if success: break
        else: print("Invalid input. Please enter a number."); time.sleep(1)
    player.display_status()
    time.sleep(2)
    trigger_random_event(player) 

    current_game_date += timedelta(days=random.randint(30, 60)) 
    adegan_kelas10_sosial = Scene(
        "Building Connections: Group Project",
        "Class is over. The teacher assigns group work. You used to always find excuses to work alone. This time, an opportunity to interact comes up.",
        {
            1: ("Invite some classmates to study together.", invite_friends_to_study),
            2: ("Focus on studying alone at home, as usual.", focus_on_studying_alone)
        }
    )
    while True:
        adegan_kelas10_sosial.display(current_game_date)
        choice = input("Your choice: ")
        if choice.isdigit():
            success, current_game_date = adegan_kelas10_sosial.make_choice(int(choice), player, current_game_date)
            if success: break
        else: print("Invalid input. Please enter a number."); time.sleep(1)
    player.display_status()
    time.sleep(2)
    trigger_random_event(player)

    current_game_date += timedelta(days=random.randint(60, 90)) 
    adegan_kelas10_extra = Scene( 
        "Beyond Academics: Free Time",
        "You have some free time this weekend. How will you spend it?",
        {
            1: ("Look for a part-time job to earn some money.", do_part_time_job_hs),
            2: ("Relax at home and recharge your energy.", relax_at_home_hs)
        }
    )
    while True:
        adegan_kelas10_extra.display(current_game_date)
        choice = input("Your choice: ")
        if choice.isdigit():
            success, current_game_date = adegan_kelas10_extra.make_choice(int(choice), player, current_game_date)
            if success: break
        else: print("Invalid input. Please enter a number."); time.sleep(1)
    player.display_status()
    time.sleep(2)
    trigger_random_event(player)

    # Adegan Kelas 11
    current_game_date = datetime(2006, 9, 1) 
    slow_type(f"\nTime flies, you're now in 11th grade. It's {current_game_date.year}. This was the time you used to be obsessed with pursuing someone, neglecting many important things.")
    time.sleep(2)
    adegan_kelas11 = Scene(
        "11th Grade: Choices of Heart and Mind",
        "There are two main paths before you: pursuing a crush that might only exhaust you, or focusing on self-development and career.",
        {
            1: ("Focus on pursuing your career and academic dreams.", pursue_dream_career),
            2: ("Try to approach 'them' who you've liked forever.", pursue_school_crush)
        }
    )
    while True:
        adegan_kelas11.display(current_game_date)
        choice = input("Your choice: ")
        if choice.isdigit():
            success, current_game_date = adegan_kelas11.make_choice(int(choice), player, current_game_date)
            if success: break
        else: print("Invalid input. Please enter a number."); time.sleep(1)
    player.display_status()
    time.sleep(2)
    trigger_random_event(player)

    # Adegan Kelas 12
    current_game_date = datetime(2007, 9, 1) 
    slow_type(f"\n12th grade, {current_game_date.year}, your last year of high school. The pressure of university entrance and the future starts to set in. This is a crucial time.")
    time.sleep(2)
    adegan_kelas12_akademik = Scene(
        "12th Grade: Path to the Future",
        "There's an opportunity to participate in a prestigious academic competition that can open many doors, but also demands high dedication.",
        {
            1: ("Join the competition and give it your all.", join_competition),
            2: ("Skip the competition, focus on regular exam prep.", decline_competition)
        }
    )
    while True:
        adegan_kelas12_akademik.display(current_game_date)
        choice = input("Your choice: ")
        if choice.isdigit():
            success, current_game_date = adegan_kelas12_akademik.make_choice(int(choice), player, current_game_date)
            if success: break
        else: print("Invalid input. Please enter a number."); time.sleep(1)
    player.display_status()
    time.sleep(2)
    trigger_random_event(player)

    current_game_date += timedelta(days=random.randint(45, 75)) 
    adegan_kelas12_sosial = Scene(
        "12th Grade: Social Involvement",
        "Various school organizations offer opportunities to develop leadership and social networks.",
        {
            1: ("Be active in school organizations and socialize a lot.", be_active_in_organization),
            2: ("Stay focused on yourself and don't get too involved in organizations.", not_active_in_organization)
        }
    )
    while True:
        adegan_kelas12_sosial.display(current_game_date)
        choice = input("Your choice: ")
        if choice.isdigit():
            success, current_game_date = adegan_kelas12_sosial.make_choice(int(choice), player, current_game_date)
            if success: break
        else: print("Invalid input. Please enter a number."); time.sleep(1)
    player.display_status()
    time.sleep(2)
    trigger_random_event(player)

    # Adegan Kuliah/Awal Karir (Usia 18-25)
    current_game_date = datetime(2008, 9, 1) 
    slow_type(f"\nYou've graduated high school. It's {current_game_date.year}, and now it's time to enter college or your early career. These choices will shape the foundation of your future.")
    time.sleep(2)
    adegan_kuliah_karir = Scene(
        "College/Early Career: Foundation of the Future",
        "You have the option to jump straight into practical work through an internship or focus entirely on theory and academics.",
        {
            1: ("Take an internship at a company that matches your career dreams.", take_internship),
            2: ("Focus on college and getting the highest grades.", focus_on_academics)
        }
    )
    while True:
        adegan_kuliah_karir.display(current_game_date)
        choice = input("Your choice: ")
        if choice.isdigit():
            success, current_game_date = adegan_kuliah_karir.make_choice(int(choice), player, current_game_date)
            if success: break
        else: print("Invalid input. Please enter a number."); time.sleep(1)
    player.display_status()
    time.sleep(2)
    trigger_random_event(player)

    current_game_date += timedelta(days=random.randint(60, 120)) # Time passes
    adegan_hubungan_awal = Scene(
        "College/Early Career: Building Relationships",
        "At this age, many people begin seeking life partners. Will you open your heart or stay focused on yourself?",
        {
            1: ("Open your heart and seek a serious relationship.", enter_serious_relationship),
            2: ("Fokus on yourself and don't rush into a relationship.", focus_on_self) # Corrected "Fokus" to "Focus"
        }
    )
    while True:
        adegan_hubungan_awal.display(current_game_date)
        choice = input("Your choice: ")
        if choice.isdigit():
            success, current_game_date = adegan_hubungan_awal.make_choice(int(choice), player, current_game_date)
            if success: break
        else: print("Invalid input. Please enter a number."); time.sleep(1)
    player.display_status()
    time.sleep(2)
    trigger_random_event(player)

    current_game_date += timedelta(days=random.randint(90, 180)) 
    adegan_early_life_wellbeing = Scene( 
        "College/Early Career: Personal Well-being",
        "You're feeling the demands of this period. How will you take care of yourself?",
        {
            1: ("Commit to regular exercise to stay healthy and energetic.", exercise),
            2: ("Let other priorities take over, neglecting your physical health.", neglect_health),
            3: ("Pick up a new hobby to relax and express yourself.", pursue_hobby)
        }
    )
    while True:
        adegan_early_life_wellbeing.display(current_game_date)
        choice = input("Your choice: ")
        if choice.isdigit():
            success, current_game_date = adegan_early_life_wellbeing.make_choice(int(choice), player, current_game_date)
            if success: break
        else: print("Invalid input. Please enter a number."); time.sleep(1)
    player.display_status()
    time.sleep(2)
    trigger_random_event(player)

    # Adegan Pertengahan Karir (Usia 25-35)
    current_game_date = datetime(2015, 1, 1) 
    slow_type(f"\nTime continues to pass, you are now in your mid-20s to early 30s. It's {current_game_date.year}. This is when your career and personal life often reach their peak.")
    time.sleep(2)
    adegan_karir_lanjut = Scene(
        "Mid-Career: Take a Risk or Play it Safe?",
        "A big opportunity comes up in your career, but it involves a huge risk. Or, you can choose to play it safe.",
        {
            1: ("Take a big risk for potentially higher rewards (e.g., start a business, big project).", take_business_risk),
            2: ("Stay stable on your current career path, playing it safe.", stabilize_in_job)
        }
    )
    while True:
        adegan_karir_lanjut.display(current_game_date)
        choice = input("Your choice: ")
        if choice.isdigit():
            success, current_game_date = adegan_karir_lanjut.make_choice(int(choice), player, current_game_date)
            if success: break
        else: print("Invalid input. Please enter a number."); time.sleep(1)
    player.display_status()
    time.sleep(2)
    trigger_random_event(player)

    current_game_date += timedelta(days=random.randint(90, 180)) 
    adegan_sosial_lanjut = Scene(
        "Mid-Career: Building Adult Relationships",
        "Will you proactively expand your social network and friendships, or stick with a more limited circle?",
        {
            1: ("Proactively make new friends and expand your social network.", make_friends),
            2: ("Continue enjoying independence and your existing social circle.", live_independently)
        }
    )
    while True:
        adegan_sosial_lanjut.display(current_game_date)
        choice = input("Your choice: ")
        if choice.isdigit():
            success, current_game_date = adegan_sosial_lanjut.make_choice(int(choice), player, current_game_date)
            if success: break
        else: print("Invalid input. Please enter a number."); time.sleep(1)
    player.display_status()
    time.sleep(2)
    trigger_random_event(player)

    # --- Game End ---
    current_game_date = datetime(2020, 7, 1) 
    slow_type(f"\n--- The Peak of Your Second Life ({current_game_date.year}) ---")
    slow_type("Time has passed. You've relived 20 years of your life. Every small and big choice has shaped who you are now.")
    time.sleep(3)

    slow_type(f"Ultimately, you reach July 1st, {current_game_date.year} again. Will the same accident occur? Or has a different path altered your destiny?")
    time.sleep(3)

    clear_screen()
    print_divider()
    print("\n## Your Life's Final Outcome\n")
    player.display_status()

    # Ending Logic
    final_mood = player.mood
    final_career = player.career_progress
    final_social = player.social
    final_courage = player.courage
    final_health = player.health
    final_mental_health = player.mental_health

    partner_level = player.relationship_status.get("Partner", {}).get("level", 0)
    friends_level = player.relationship_status.get("New Friends", {}).get("level", 0)

    slow_type("\nDigging through your new memories...")
    for memory in player.future_memories:
        slow_type(f"- {memory}")
        time.sleep(0.5)

    slow_type("\nHolding your breath, you look around. The street is busy. You pass the same intersection where the accident used to happen.")
    time.sleep(3)

    # Ending Conditions
    if (final_courage >= 30 and final_career >= 90 and final_social >= 70 and
        final_mood >= 70 and final_health >= 70 and final_mental_health >= 70 and
        (partner_level >= 70 or friends_level >= 70)):
        slow_type("Suddenly, a loud horn! A truck speeds toward you! But somehow, your reflexes are incredible! You jump, managing to avoid the collision by mere inches. Sweat beads on your forehead, but you're safe!")
        slow_type("You look around. The family and friends you've built during this life run to you, first worried, then overwhelmingly relieved.")
        slow_type("You have successfully changed your destiny! Your life is full of meaning, surrounded by loving people. You are no longer the lonely, unfulfilled person you once were.")
        player.ending = "Perfect Redemption"
        slow_type("\nCongratulations! You have lived a full and meaningful life.")
    elif (final_courage >= 20 and final_career >= 60 and final_social >= 40 and
          final_mood >= 50 and final_health >= 50 and final_mental_health >= 50):
        slow_type("The screech of tires! A car drives too close, almost brushing you. But you manage to dodge it with only minor scrapes. Nothing fatal!")
        slow_type("You might not be perfect, but you've made significant positive changes. You have a decent career, some meaningful connections, and a healthier mindset. Your life is much better than before.")
        player.ending = "Significant Change"
        slow_type("\nYou have significantly changed the course of your life. Well done!")
    else:
        slow_type("That loud horn... the screech of brakes... and darkness. For a fleeting moment, you see that empty life again, and bitter memories of the choices you didn't change. You failed to alter destiny...")
        slow_type("Just like before, you lie there, seeing the same light. But this time, there's no choice. Only a soft whisper: 'A chance was given. But the choices were still yours.'")
        player.ending = "Fate Repeats"
        slow_type("\nUnfortunately, your fate has repeated. However, every choice is still a lesson.")

    print_divider()
    slow_type(f"\nStory End: {player.ending}")
    slow_type("Thank you for playing 'LIFE RECYCLE'!")
    print_divider()

    print("\nDo you want to see your final detailed statistics? (yes/no)")
    if input().lower() == 'yes':
        player.display_status()
        print("\nMemories of Change:")
        for memory in player.future_memories:
            print(f"- {memory}")


if __name__ == "__main__":
    try:
        main_game()
    except KeyboardInterrupt:
        print("\nGame stopped. See you!")