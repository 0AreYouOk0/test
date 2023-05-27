import json

def take_quiz(questions):
    total_score = 0
    for question in questions:
        print(question['question'])
        options = question['options']
        for i, option in enumerate(options):
            print(f"{i+1}. {option['option']}")
        
        while True:
            try:
                answer = int(input("請選擇您的答案（輸入選項前的數字）："))
                if 1 <= answer <= len(options):
                    break
                else:
                    print("請輸入有效的選項編號！")
            except ValueError:
                print("請輸入數字！")
        
        score = options[answer-1]['score']
        total_score += score
        print()
    
    return total_score

def main():
    with open('quiz.json', 'r',encoding="utf-8") as file:
        quiz_data = json.load(file)
    
    questions = quiz_data['questions']
    score = take_quiz(questions)
    
    print(f"您的總分為：{score}分")
    # 根據得分可以添加相應的結果顯示邏輯

if __name__ == '__main__':
    main()
