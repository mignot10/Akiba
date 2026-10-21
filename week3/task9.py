def display_question(q_num:int, question_data: dict):
    print(f"\nQuestion {q_num}: {question_data['question']}")
    for idx, option in enumerate(question_data['options'], start = 1):
        print(f' {idx}. {option}')

def  validate_answer (user_input: str, num_options: int):
    user_input = user_input.strip()
    if not user_input:
        return False

    if user_input.isdigit():
        choice_num = int(user_input)
        return 1<= choice_num <= num_options
    return False

def check_answer(user_input: str, question_data: dict):
    user_input = user_input.strip()
    correct_ans = question_data['correct'].strip()

    #if the user typed a number, map it to the option text
    if user_input.isdigit():
        choice_idx = int(user_input) - 1
        if 0 <= choice_idx < len(question_data['options']):
            selected_option = question_data['options'][choice_idx]
            return selected_option.lower() == correct_ans.lower()
        
        # Otherwise, check direct string comparison (case-insensitive)
        return user_input.lower() == correct_ans.lower()

def update_score(is_correct, current_score):
    return current_score + 1 if is_correct else current_score

def get_result_category(percentage):
    if percentage == 100.0:
        id = "Expert / Master"
    elif percentage >= 80.0:
        id = "Proficient"
    elif percentage >= 50.0:
        id = "Intermediate"
    else:
        id = "Needs Improvement"
    return id

def display_final_result(score, total_questions):
    percentage = (score / total_questions) * 100.0
    incorrect = total_questions - score
    category = get_result_category(percentage)
    
    print("\n" + "=" * 40)
    print("          QUIZ FINAL RESULTS          ")
    print("=" * 40)
    print(f"Total Questions : {total_questions}")
    print(f"Correct Answers : {score}")
    print(f"Incorrect Answers : {incorrect}")
    print(f"Final Percentage: {percentage:.2f}%")
    print(f"Performance Tier: {category}")
    print("=" * 40)

def run_quiz(quiz_bank):
    while True:
        score = 0
        total_questions = len(quiz_bank)
        
        print("\nStarting Quiz Game... Good luck!")
        
        for idx, q_data in enumerate(quiz_bank, start=1):
            display_question(idx, q_data)
            
            # Prompt loop until valid input is received

            while True:
                user_input = input("\nEnter your answer (number or text): ")
                if validate_answer(user_input, len(q_data["options"])):
                    break
                print("Invalid option or empty input. Please enter a valid choice number.") 

            #Check correctness and update score
            is_correct = check_answer(user_input, q_data)
            score = update_score(is_correct, score)

            if is_correct:
                print("Correct!\n")
            else: 
                print(f"Incorrect. The correct answer was: {q_data['correct']}\n")

        #display summary report
        display_final_result(score,total_questions)

        #allow replay without restarting python
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again not in ['y', 'yes']:
            print("\nThank you for playing! Goodbye.")
            break


if __name__ == "__main__":
    sample_questions = [
        {
            "question": "Which programming language is known for its readability and indentation syntax?",
            "options": ["Java", "Python", "C++", "Assembly"],
            "correct": "Python"
        },
        {
            "question": "What is the time complexity of binary search on a sorted array?",
            "options": ["O(n)", "O(n^2)", "O(log n)", "O(1)"],
            "correct": "O(log n)"
        },
        {
            "question": "Which protocol is primarily used to securely transmit web pages over the internet?",
            "options": ["HTTP", "FTP", "HTTPS", "SMTP"],
            "correct": "HTTPS"
        },
        {
            "question": "In database management, what does SQL stand for?",
            "options": ["Structured Query Language", "Simple Query Loop", "Sequential Quality List", "System Quantitative Logic"],
            "correct": "Structured Query Language"
        },
        {
            "question": "Which data structure operates on a Last-In, First-Out (LIFO) basis?",
            "options": ["Queue", "Stack", "Array", "Graph"],
            "correct": "Stack"
        }
    ]
    
    # Run the engine
    run_quiz(sample_questions)
        