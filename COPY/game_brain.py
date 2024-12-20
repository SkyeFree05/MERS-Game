import random

class QuizBrain:
    def __init__(self):
        self.questions = {
            "easy": [
    {"question": "What is the capital of France?", "options": ["London", "Paris", "Rome", "Berlin"], "answer": 1},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": 1},
    {"question": "What color is the sky on a clear day?", "options": ["Red", "Blue", "Green", "Yellow"], "answer": 1},
    {"question": "Which animal is known as man's best friend?", "options": ["Cat", "Dog", "Horse", "Bird"], "answer": 1},
    {"question": "How many continents are there?", "options": ["5", "6", "7", "8"], "answer": 2},
    {"question": "What is the boiling point of water?", "options": ["90°C", "95°C", "100°C", "105°C"], "answer": 2},
    {"question": "What fruit is known for keeping doctors away?", "options": ["Banana", "Orange", "Apple", "Grapes"], "answer": 2},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": 1},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Mark Twain", "William Shakespeare", "Charles Dickens", "Ernest Hemingway"], "answer": 1},
    {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "answer": 1},
    {"question": "What is the smallest unit of life?", "options": ["Atom", "Molecule", "Cell", "Organ"], "answer": 2},
    {"question": "What is the chemical symbol for water?", "options": ["H2O", "CO2", "O2", "NaCl"], "answer": 0},
    {"question": "Who is the founder of Microsoft?", "options": ["Steve Jobs", "Bill Gates", "Elon Musk", "Mark Zuckerberg"], "answer": 1},
    {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": 2},
    {"question": "What is the main ingredient in guacamole?", "options": ["Tomato", "Lettuce", "Avocado", "Onion"], "answer": 2},
    {"question": "How many days are there in a leap year?", "options": ["364", "365", "366", "367"], "answer": 2},
    {"question": "Who painted the Mona Lisa?", "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], "answer": 2},
    {"question": "What is the fastest land animal?", "options": ["Lion", "Tiger", "Cheetah", "Leopard"], "answer": 2},
    {"question": "What is the capital of Japan?", "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"], "answer": 2},
    {"question": "How many sides does a hexagon have?", "options": ["5", "6", "7", "8"], "answer": 1},
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": 3},
    {"question": "Who invented the telephone?", "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Albert Einstein"], "answer": 1},
    {"question": "What is the capital of Italy?", "options": ["Venice", "Rome", "Florence", "Naples"], "answer": 1},
    {"question": "What is the smallest planet in our solar system?", "options": ["Mercury", "Venus", "Mars", "Earth"], "answer": 0},
    {"question": "What is the primary language spoken in Brazil?", "options": ["Spanish", "Portuguese", "French", "Italian"], "answer": 1},
    {"question": "How many bones are there in the adult human body?", "options": ["204", "206", "208", "210"], "answer": 1},
    {"question": "What is the process by which plants make their food?", "options": ["Photosynthesis", "Respiration", "Digestion", "Fermentation"], "answer": 0},
    {"question": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Pb", "Fe"], "answer": 0},
    {"question": "Who wrote 'Harry Potter'?", "options": ["J.R.R. Tolkien", "J.K. Rowling", "George R.R. Martin", "Stephen King"], "answer": 1},
    {"question": "What is the largest continent?", "options": ["Africa", "Asia", "Europe", "North America"], "answer": 1},
    {"question": "What is the hottest planet in our solar system?", "options": ["Mercury", "Venus", "Mars", "Earth"], "answer": 1},
    {"question": "What is the capital of the United Kingdom?", "options": ["Manchester", "Liverpool", "London", "Birmingham"], "answer": 2},
    {"question": "Who is known as the Father of Computers?", "options": ["Alan Turing", "Bill Gates", "Charles Babbage", "Steve Jobs"], "answer": 2},
    {"question": "What is the main gas found in the air we breathe?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": 1},
    {"question": "What is the currency of Japan?", "options": ["Won", "Yen", "Dollar", "Euro"], "answer": 1},
    {"question": "Which country is known as the Land of the Rising Sun?", "options": ["China", "Japan", "South Korea", "Thailand"], "answer": 1},
    {"question": "What is the smallest country in the world?", "options": ["Monaco", "Vatican City", "Malta", "Liechtenstein"], "answer": 1},
    {"question": "What is the primary ingredient in a Caesar Salad?", "options": ["Spinach", "Kale", "Romaine Lettuce", "Arugula"], "answer": 2},
    {"question": "How many states are there in the United States?", "options": ["48", "49", "50", "51"], "answer": 2},
    {"question": "What is the symbol for the element Iron?", "options": ["Ir", "Fe", "I", "F"], "answer": 1},
    {"question": "Which bird is known for its colorful plumage?", "options": ["Penguin", "Peacock", "Parrot", "Eagle"], "answer": 1},
    {"question": "What is the main language spoken in Canada?", "options": ["French", "Spanish", "English", "Italian"], "answer": 2},
    {"question": "What is the tallest mountain in the world?", "options": ["K2", "Mount Everest", "Kangchenjunga", "Lhotse"], "answer": 1},
    {"question": "What is the hardest natural substance on Earth?", "options": ["Gold", "Iron", "Diamond", "Quartz"], "answer": 2},
    {"question": "What is the capital of Australia?", "options": ["Sydney", "Melbourne", "Perth", "Canberra"], "answer": 3},
    {"question": "Who discovered penicillin?", "options": ["Marie Curie", "Alexander Fleming", "Louis Pasteur", "Gregor Mendel"], "answer": 1},
    {"question": "What is the longest river in the world?", "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"], "answer": 1},
    {"question": "What is the basic unit of currency in the UK?", "options": ["Dollar", "Euro", "Pound", "Yen"], "answer": 2},
    {"question": "What is the largest bone in the human body?", "options": ["Femur", "Tibia", "Humerus", "Radius"], "answer": 0}
],
            "normal": [
    {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": 2}, 
    {"question": "Who painted the ceiling of the Sistine Chapel?", "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"], "answer": 1}, 
    {"question": "What is the chemical symbol for potassium?", "options": ["P", "K", "Pt", "Po"], "answer": 1}, 
    {"question": "In which year did the Titanic sink?", "options": ["1905", "1912", "1920", "1930"], "answer": 1}, 
    {"question": "Who is the author of '1984'?", "options": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "Jules Verne"], "answer": 0}, 
    {"question": "What is the hardest natural substance on Earth?", "options": ["Gold", "Iron", "Diamond", "Platinum"], "answer": 2}, 
    {"question": "Who was the first man to walk on the moon?", "options": ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Michael Collins"], "answer": 1}, 
    {"question": "Which gas is most abundant in Earth's atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Argon"], "answer": 1},
    {"question": "What is the largest bone in the human body?", "options": ["Skull", "Femur", "Spine", "Pelvis"], "answer": 1}, 
    {"question": "What is the capital of Canada?", "options": ["Toronto", "Vancouver", "Montreal", "Ottawa"], "answer": 3},
    {"question": "What is the smallest prime number?", "options": ["1", "2", "3", "5"], "answer": 1}, 
    {"question": "Which artist painted 'Starry Night'?", "options": ["Pablo Picasso", "Vincent van Gogh", "Claude Monet", "Salvador Dalí"], "answer": 1}, 
    {"question": "In which country are the Pyramids of Giza located?", "options": ["Mexico", "Peru", "Egypt", "China"], "answer": 2}, 
    {"question": "What is the speed of light?", "options": ["300,000 km/s", "150,000 km/s", "450,000 km/s", "600,000 km/s"], "answer": 0}, 
    {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["Ernest Hemingway", "Harper Lee", "Mark Twain", "F. Scott Fitzgerald"], "answer": 1}, 
    {"question": "Which country hosted the 2016 Summer Olympics?", "options": ["China", "UK", "Brazil", "Russia"], "answer": 2}, 
    {"question": "What is the powerhouse of the cell?", "options": ["Nucleus", "Ribosome", "Mitochondria", "Chloroplast"], "answer": 2}, 
    {"question": "What is the chemical formula for table salt?", "options": ["NaCl", "KCl", "CaCl2", "MgCl2"], "answer": 0}, 
    {"question": "Who discovered penicillin?", "options": ["Marie Curie", "Alexander Fleming", "Louis Pasteur", "Gregor Mendel"], "answer": 1},
    {"question": "What is the capital of Australia?", "options": ["Sydney", "Melbourne", "Canberra", "Perth"], "answer": 2}, 
    {"question": "Which planet is known as the Morning Star?", "options": ["Mars", "Venus", "Mercury", "Jupiter"], "answer": 1}, 
    {"question": "Who was the first President of the United States?", "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"], "answer": 2},
    {"question": "What is the currency of India?", "options": ["Dollar", "Rupee", "Euro", "Yen"], "answer": 1}, 
    {"question": "What is the capital of Russia?", "options": ["Moscow", "St. Petersburg", "Novosibirsk", "Sochi"], "answer": 0}, 
    {"question": "Who wrote 'The Great Gatsby'?", "options": ["Ernest Hemingway", "F. Scott Fitzgerald", "Mark Twain", "J.D. Salinger"], "answer": 1}, 
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": 3}, 
    {"question": "What is the chemical symbol for oxygen?", "options": ["O", "O2", "O3", "Ox"], "answer": 0}, 
    {"question": "In which year did World War II end?", "options": ["1943", "1944", "1945", "1946"], "answer": 2}, 
    {"question": "What is the tallest animal in the world?", "options": ["Elephant", "Giraffe", "Kangaroo", "Lion"], "answer": 1}, 
    {"question": "What is the boiling point of water in Fahrenheit?", "options": ["200°F", "210°F", "220°F", "212°F"], "answer": 3}, 
    {"question": "Which country is the largest producer of coffee?", "options": ["Colombia", "Vietnam", "Brazil", "Ethiopia"], "answer": 2}, 
    {"question": "What is the largest desert in the world?", "options": ["Sahara", "Arabian", "Gobi", "Antarctic"], "answer": 3}, 
    {"question": "Who invented the light bulb?", "options": ["Nikola Tesla", "Alexander Graham Bell", "Thomas Edison", "George Westinghouse"], "answer": 2}, 
    {"question": "What is the capital of Spain?", "options": ["Barcelona", "Madrid", "Seville", "Valencia"], "answer": 1}, 
    {"question": "What is the most spoken language in the world?", "options": ["English", "Spanish", "Mandarin", "Hindi"], "answer": 2}, 
    {"question": "What is the chemical symbol for silver?", "options": ["Si", "Au", "Ag", "Sn"], "answer": 2}, 
    {"question": "What is the main ingredient in traditional Japanese miso soup?", "options": ["Soybeans", "Rice", "Tofu", "Fish"], "answer": 0}, 
    {"question": "What is the highest mountain in North America?", "options": ["Mount Whitney", "Mount Elbert", "Denali", "Pikes Peak"], "answer": 2}, 
    {"question": "Who was the first woman to fly solo across the Atlantic?", "options": ["Amelia Earhart", "Harriet Quimby", "Bessie Coleman", "Jacqueline Cochran"], "answer": 0}, 
    {"question": "What is the most abundant element in the universe?", "options": ["Oxygen", "Carbon", "Hydrogen", "Nitrogen"], "answer": 2}, 
    {"question": "What is the chemical formula for carbon dioxide?", "options": ["CO", "CO2", "C2O", "CO3"], "answer": 1}, 
    {"question": "Who painted 'The Last Supper'?", "options": ["Michelangelo", "Leonardo da Vinci", "Raphael", "Donatello"], "answer": 1}, 
    {"question": "What is the capital of Germany?", "options": ["Berlin", "Munich", "Frankfurt", "Hamburg"], "answer": 0}, 
    {"question": "What is the largest organ in the human body?", "options": ["Heart", "Lungs", "Skin", "Liver"], "answer": 2}, 
    {"question": "In which country is the Taj Mahal located?", "options": ["Pakistan", "India", "Bangladesh", "Nepal"], "answer": 1}, 
    {"question": "What is the currency of China?", "options": ["Yen", "Won", "Rupee", "Yuan"], "answer": 3}, 
    {"question": "Which planet is closest to the sun?", "options": ["Earth", "Venus", "Mercury", "Mars"], "answer": 2}, 
    {"question": "Who wrote the 'Iliad' and the 'Odyssey'?", "options": ["Homer", "Virgil", "Ovid", "Sophocles"], "answer": 0}, 
    {"question": "What is the capital of Brazil?", "options": ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"], "answer": 2}

],
            "hard": [
   {"question": "What is the longest river in the world?", "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"], "answer": 1}, 
   {"question": "Who developed the theory of general relativity?", "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"], "answer": 1}, 
   {"question": "What element does 'O' represent on the periodic table?", "options": ["Osmium", "Oxygen", "Oganesson", "Oxalate"], "answer": 1}, 
   {"question": "What is the capital of Iceland?", "options": ["Oslo", "Reykjavik", "Helsinki", "Copenhagen"], "answer": 1}, 
   {"question": "What is the smallest country in the world by area?", "options": ["Monaco", "San Marino", "Liechtenstein", "Vatican City"], "answer": 3}, 
   {"question": "Which planet is known for its ring system?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": 3}, 
   {"question": "Who is considered the father of modern physics?", "options": ["Isaac Newton", "Albert Einstein", "Niels Bohr", "Stephen Hawking"], "answer": 0}, 
   {"question": "What is the primary language spoken in Switzerland?", "options": ["French", "German", "Italian", "Romansh"], "answer": 1}, 
   {"question": "Who wrote 'Pride and Prejudice'?", "options": ["Charlotte Brontë", "Emily Dickinson", "Jane Austen", "Louisa May Alcott"], "answer": 2}, 
   {"question": "What is the powerhouse of the cell?", "options": ["Nucleus", "Mitochondria", "Ribosome", "Chloroplast"], "answer": 1}, 
   {"question": "What is the square root of 144?", "options": ["10", "11", "12", "13"], "answer": 2}, 
   {"question": "What is the currency of South Korea?", "options": ["Yen", "Won", "Dollar", "Euro"], "answer": 1}, 
   {"question": "What is the chemical formula for ammonia?", "options": ["NH3", "H2O", "CO2", "H2O2"], "answer": 0}, 
   {"question": "Who wrote 'The Odyssey'?", "options": ["Homer", "Virgil", "Ovid", "Sophocles"], "answer": 0}, 
   {"question": "What is the capital of Turkey?", "options": ["Istanbul", "Ankara", "Izmir", "Antalya"], "answer": 1}, 
   {"question": "What is the largest internal organ in the human body?", "options": ["Heart", "Liver", "Lungs", "Kidneys"], "answer": 1}, 
   {"question": "Which element has the atomic number 6?", "options": ["Oxygen", "Carbon", "Nitrogen", "Sulfur"], "answer": 1}, 
   {"question": "Who painted the Mona Lisa?", "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"], "answer": 0}, 
   {"question": "What is the capital of Thailand?", "options": ["Bangkok", "Phuket", "Chiang Mai", "Pattaya"], "answer": 0}, 
   {"question": "Who discovered gravity?", "options": ["Galileo Galilei", "Isaac Newton", "Albert Einstein", "Nikola Tesla"], "answer": 1}, 
   {"question": "Which planet is closest to the sun?", "options": ["Venus", "Mars", "Mercury", "Earth"], "answer": 2}, 
   {"question": "What is the capital of Finland?", "options": ["Oslo", "Stockholm", "Copenhagen", "Helsinki"], "answer": 3}, 
   {"question": "What is the chemical symbol for lead?", "options": ["Pb", "Fe", "Au", "Hg"], "answer": 0}, 
   {"question": "Who wrote 'Moby-Dick'?", "options": ["Herman Melville", "Nathaniel Hawthorne", "Mark Twain", "Henry James"], "answer": 0}, 
   {"question": "What is the tallest building in the world?", "options": ["Shanghai Tower", "Abraj Al-Bait Clock Tower", "One World Trade Center", "Burj Khalifa"], "answer": 3}, 
   {"question": "What is the most populous country in the world?", "options": ["India", "United States", "China", "Indonesia"], "answer": 2}, 
   {"question": "What is the distance from the Earth to the Sun?", "options": ["93 million miles", "150 million kilometers", "93 million kilometers", "150 million miles"], "answer": 0}, 
   {"question": "What is the hardest mineral?", "options": ["Quartz", "Diamond", "Topaz", "Corundum"], "answer": 1}, 
   {"question": "What is the largest country by area?", "options": ["Canada", "United States", "China", "Russia"], "answer": 3}, 
   {"question": "Who wrote 'War and Peace'?", "options": ["Fyodor Dostoevsky", "Leo Tolstoy", "Anton Chekhov", "Alexander Pushkin"], "answer": 1}, 
   {"question": "What is the primary component of natural gas?", "options": ["Methane", "Ethane", "Propane", "Butane"], "answer": 0}, 
   {"question": "What is the second most populous country in the world?", "options": ["United States", "India", "China", "Indonesia"], "answer": 1}, 
   {"question": "Who developed the theory of evolution?", "options": ["Albert Einstein", "Isaac Newton", "Charles Darwin", "Nikola Tesla"], "answer": 2}, 
   {"question": "What is the capital of Argentina?", "options": ["Buenos Aires", "São Paulo", "Lima", "Santiago"], "answer": 0}, 
   {"question": "Who painted 'The Starry Night'?", "options": ["Vincent van Gogh", "Claude Monet", "Pablo Picasso", "Salvador Dalí"], "answer": 0}, 
   {"question": "What is the chemical symbol for sodium?", "options": ["Na", "S", "N", "Si"], "answer": 0}, 
   {"question": "What is the tallest mountain in the world?", "options": ["K2", "Kangchenjunga", "Lhotse", "Mount Everest"], "answer": 3}, 
   {"question": "What is the longest bone in the human body?", "options": ["Femur", "Tibia", "Fibula", "Humerus"], "answer": 0}, 
   {"question": "Who was the first woman to win a Nobel Prize?", "options": ["Marie Curie", "Rosalind Franklin", "Jane Goodall", "Ada Lovelace"], "answer": 0}, 
   {"question": "What is the primary language spoken in Australia?", "options": ["French", "German", "English", "Spanish"], "answer": 2}, 
   {"question": "What is the capital of Portugal?", "options": ["Lisbon", "Madrid", "Barcelona", "Rome"], "answer": 0}, 
   {"question": "What is the speed of sound?", "options": ["343 m/s", "299,792 m/s", "1235 km/h", "186,282 m/s"], "answer": 0}, 
   {"question": "Who wrote 'The Catcher in the Rye'?", "options": ["J.D. Salinger", "F. Scott Fitzgerald", "Ernest Hemingway", "George Orwell"], "answer": 0}, 
   {"question": "What is the most common gas in the Earth's atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Hydrogen", "Nitrogen"], "answer": 3}, 
   {"question": "What is the chemical formula for sulfuric acid?", "options": ["H2SO4", "HCl", "HNO3", "H2O"], "answer": 0}, 
   {"question": "Who was the first man to reach the South Pole?", "options": ["Robert Falcon Scott", "Ernest Shackleton", "Roald Amundsen", "Edmund Hillary"], "answer": 2}, 
   {"question": "What is the capital of Kenya?", "options": ["Nairobi", "Cape Town", "Johannesburg", "Lagos"], "answer": 0}, 
   {"question": "Who wrote 'Great Expectations'?", "options": ["Charles Dickens", "Jane Austen", "Mark Twain", "William Shakespeare"], "answer": 0}
],
        }
        self.score = 0
        self.lives = 3
        self.current_question_index = 0
        self.difficulty = "easy"  # Default difficulty
        self.questions_list = [] #Store questions here to track total questions
        self.load_questions()

    def load_questions(self):
        self.questions_list = self.questions[self.difficulty].copy() #Create a copy to avoid modifying original
        random.shuffle(self.questions_list)


    def start_quiz(self, difficulty): #Added a start_quiz method
        self.difficulty = difficulty
        self.load_questions()

    def has_next_question(self):
        return self.current_question_index < len(self.questions_list)

    def get_next_question(self):
        if self.has_next_question():
            current_question = self.questions_list[self.current_question_index]
            return {
                "question": current_question["question"],
                "options": current_question["options"],
            }
        return None

    def check_answer(self, selected_option):
        correct_answer_index = self.questions_list[self.current_question_index]["answer"]
        is_correct = selected_option == correct_answer_index
        if is_correct:
            self.score += 1
        else:
            self.lives -= 1
        self.current_question_index += 1
        return is_correct

    def reset(self):
        self.score = 0
        self.lives = 3
        self.current_question_index = 0
        self.load_questions()
