import pygame
import random

turn = random.randint(1,2)
if turn == 1:
    print("User's turn")
else:
    print("PC's turn")
    
char = input("select any one character X or O: ")

white = (255,255,255)

pygame.init()
window = pygame.display.set_mode((200,200))
pygame.display.set_caption("Tic_Tac_Toe")
# Vertical lines : 
pygame.draw.line(window, white, (75,25),(75,175))
pygame.draw.line(window, white, (125,25),(125,175))
# Horizontal lines :
pygame.draw.line(window, white, (25,75),(175,75))
pygame.draw.line(window, white, (25,125),(175,125))

tracker = [0,0,0,0,0,0,0,0,0]
game_end = []
game_ended = 0

def human():
    end_loop = 0
    if winner_check() == "X":
        end_loop = end_loop + 1
        print("Character X won")
    elif winner_check() == "O":
        print("Character O won")
        end_loop = end_loop + 1
    game_play = True
    while game_play:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_play = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
            
                # 1st slot entry
                if pos[0] <= 75 and pos[1] <= 75:
                    if char == "X" and tracker[0] == 0 and end_loop == 0:
                        pygame.draw.line(window, white, (25,25),(75,75))
                        pygame.draw.line(window, white, (25,75),(75,25))
                        tracker.pop(0)
                        tracker.insert(0,"X")
                        print(tracker)
                        game_end.append(1)
                        if len(game_end) != 9:
                            pc()
                        elif len(game_end) == 9:
                            if winner_check() == "X":
                                print("Character X won")
                            elif winner_check == "O":
                                print("Charatcer O won")
                            else:
                                print("game over")
                    if char == "O" and tracker[0] == 0 and end_loop == 0:
                        pygame.draw.circle(window, white, (50,50), 25)
                        tracker.pop(0)
                        tracker.insert(0,"O")
                        print(tracker)
                        game_end.append(1)
                        if len(game_end) != 9:
                            pc()
                        elif len(game_end) == 9:
                            if winner_check() == "X":
                                print("Character X won")
                            elif winner_check == "O":
                                print("Charatcer O won")
                            else:
                                print("game over")
                    if tracker[0] != 0 and len(game_end) != 9:
                        print("slot taken try again: ")
                        human()
                        
                # 2st slot entry
                if pos[0] >= 75 and pos[0] <= 125 and pos[1] <= 75:
                    if char == "X" and tracker[1] == 0 and end_loop == 0:
                        pygame.draw.line(window, white, (75,75),(125,25))
                        pygame.draw.line(window, white, (75,25),(125,75))
                        tracker.pop(1)
                        tracker.insert(1,"X")
                        print(tracker)
                        game_end.append(1)
                        if len(game_end) != 9:
                            pc()
                        elif len(game_end) == 9:
                            print("game over")
                    if char == "O" and tracker[1] == 0 and end_loop == 0:
                        pygame.draw.circle(window, white, (100,50), 25)
                        tracker.pop(1)
                        tracker.insert(1,"O")
                        print(tracker)
                        game_end.append(1)
                        if len(game_end) != 9:
                            pc()
                        elif len(game_end) == 9:
                            if winner_check() == "X":
                                print("Character X won")
                            elif winner_check == "O":
                                print("Charatcer O won")
                            else:
                                print("game over")
                    if tracker[1] != 0 and len(game_end) != 9:
                        print("slot taken try again: ")
                        human()
                            
                # 3st slot entry
                if pos[0] >= 125 and pos[1] <= 75:
                    if char == "X" and tracker[2] == 0 and end_loop == 0:
                        pygame.draw.line(window, white, (125,75),(175,25))
                        pygame.draw.line(window, white, (125,25),(175,75))
                        tracker.pop(2)
                        tracker.insert(2,"X")
                        print(tracker)
                        game_end.append(1)
                        if len(game_end) != 9:
                            pc()
                        elif len(game_end) == 9:
                            if winner_check() == "X":
                                print("Character X won")
                            elif winner_check == "O":
                                print("Charatcer O won")
                            else:
                                print("game over")
                    if char == "O" and tracker[2] == 0 and end_loop == 0:
                        pygame.draw.circle(window, white, (150,50), 25)
                        tracker.pop(2)
                        tracker.insert(2,"O")
                        print(tracker)
                        game_end.append(1)
                        if len(game_end) != 9:
                            pc()
                        elif len(game_end) == 9:
                            if winner_check() == "X":
                                print("Character X won")
                            elif winner_check == "O":
                                print("Charatcer O won")
                            else:
                                print("game over")
                    if tracker[2] != 0 and len(game_end) != 9:
                        print("slot taken try again: ")
                        human()
                        
                # 4st slot entry        
                if pos[0] <= 75 and pos[1] >= 75 and pos[1] <= 125:
                    if char == "X" and tracker[3] == 0 and end_loop == 0:
                        pygame.draw.line(window, white, (25,125),(75,75))
                        pygame.draw.line(window, white, (75,125),(25,75))
                        tracker.pop(3)
                        tracker.insert(3,"X")
                        game_end.append(1)
                        if len(game_end) != 9:
                            pc()
                        elif len(game_end) == 9:
                            if winner_check() == "X":
                                print("Character X won")
                            elif winner_check == "O":
                                print("Charatcer O won")
                            else:
                                print("game over")
                    if char == "O" and tracker[3] == 0 and end_loop == 0:
                        pygame.draw.circle(window, white, (50,100), 25)
                        tracker.pop(3)
                        tracker.insert(3,"O")
                        game_end.append(1)
                        if len(game_end) != 9:
                            pc()
                        elif len(game_end) == 9:
                            if winner_check() == "X":
                                print("Character X won")
                            elif winner_check == "O":
                                print("Charatcer O won")
                            else:
                                print("game over")
                    if tracker[3] != 0 and len(game_end) != 9:
                        print("slot taken try again: ")
                        human()
                        
                # 5st slot entry
                if pos[0] >= 75 and pos[0] <= 125 and pos[1] >= 75 and pos[1] <= 125:
                    if char == "X" and tracker[4] == 0 and end_loop == 0:
                        pygame.draw.line(window, white, (75,125),(125,75))
                        pygame.draw.line(window, white, (75,75),(125,125))
                        tracker.pop(4)
                        tracker.insert(4,"X")
                        game_end.append(1)
                        if len(game_end) != 9:
                            pc()
                        elif len(game_end) == 9:
                            if winner_check() == "X":
                                print("Character X won")
                            elif winner_check == "O":
                                print("Charatcer O won")
                            else:
                                print("game over")
                    if char == "O" and tracker[4] == 0 and end_loop == 0:
                        pygame.draw.circle(window, white, (100,100), 25)
                        tracker.pop(4)
                        tracker.insert(4,"O")
                        game_end.append(1)
                        if len(game_end) != 9:
                            pc()
                        elif len(game_end) == 9:
                            if winner_check() == "X":
                                print("Character X won")
                            elif winner_check == "O":
                                print("Charatcer O won")
                            else:
                                print("game over")
                    if tracker[4] != 0 and len(game_end) != 9:
                        print("slot taken try again: ")
                        human()
                        
                        
                # 6st slot entry
                if pos[0] >= 125 and pos[1] >= 75 and pos[1] <= 125:
                    if char == "X" and tracker[5] == 0 and end_loop == 0:
                        pygame.draw.line(window, white, (125,125),(175,75))
                        pygame.draw.line(window, white, (175,125),(125,75))
                        tracker.pop(5)
                        tracker.insert(5,"X")
                        game_end.append(1)
                        if len(game_end) != 9:
                            pc()
                        elif len(game_end) == 9:
                            if winner_check() == "X":
                                print("Character X won")
                            elif winner_check == "O":
                                print("Charatcer O won")
                            else:
                                print("game over")
                    if char == "O" and tracker[5] == 0 and end_loop == 0:
                        pygame.draw.circle(window, white, (150,100), 25)
                        tracker.pop(5)
                        tracker.insert(5,"O")
                        game_end.append(1)
                        if len(game_end) != 9:
                            pc()
                        elif len(game_end) == 9:
                            if winner_check() == "X":
                                print("Character X won")
                            elif winner_check == "O":
                                print("Charatcer O won")
                            else:
                                print("game over")
                    if tracker[5] != 0 and len(game_end) != 9:
                        print("slot taken try again: ")
                        human()
                        
                        
                # 7st slot entry
                if pos[0] <= 75 and pos[1] >= 125:
                    if char == "X" and tracker[6] == 0 and end_loop == 0:
                        pygame.draw.line(window, white, (75,175),(25,125))
                        pygame.draw.line(window, white, (75,125),(25,175))
                        tracker.pop(6)
                        tracker.insert(6,"X")
                        game_end.append(1)
                        if len(game_end) != 9:
                            pc()
                        elif len(game_end) == 9:
                            if winner_check() == "X":
                                print("Character X won")
                            elif winner_check == "O":
                                print("Charatcer O won")
                            else:
                                print("game over")
                    if char == "O" and tracker[6] == 0 and end_loop == 0:
                        pygame.draw.circle(window, white, (50,150), 25)
                        tracker.pop(6)
                        tracker.insert(6,"O")
                        game_end.append(1)
                        if len(game_end) != 9:
                            pc()
                        elif len(game_end) == 9:
                            if winner_check() == "X":
                                print("Character X won")
                            elif winner_check == "O":
                                print("Charatcer O won")
                            else:
                                print("game over")
                    if tracker[6] != 0 and len(game_end) != 9:
                        print("slot taken try again: ")
                        human()
                        
                # 8st slot entry
                if pos[0] >= 75 and pos[0] and pos[0] < 125 and pos[1] >= 125:
                    if char == "X" and tracker[7] == 0 and end_loop == 0:
                        pygame.draw.line(window, white, (75,125),(125,175))
                        pygame.draw.line(window, white, (75,175),(125,125))
                        tracker.pop(7)
                        tracker.insert(7,"X")
                        game_end.append(1)
                        if len(game_end) != 9:
                            pc()
                        elif len(game_end) == 9:
                            if winner_check() == "X":
                                print("Character X won")
                            elif winner_check == "O":
                                print("Charatcer O won")
                            else:
                                print("game over")
                    if char == "O" and tracker[7] == 0 and end_loop == 0:
                        pygame.draw.circle(window, white, (100,150), 25)
                        tracker.pop(7)
                        tracker.insert(7,"O")
                        game_end.append(1)
                        if len(game_end) != 9:
                            pc()
                        elif len(game_end) == 9:
                            if winner_check() == "X":
                                print("Character X won")
                            elif winner_check == "O":
                                print("Charatcer O won")
                            else:
                                print("game over")
                    if tracker[7] != 0 and len(game_end) != 9:
                        print("slot taken try again: ")
                        human()
                        
                # 9st slot entry
                if pos[0] >= 125 and pos[0] <= 175 and pos[1] >= 125:
                    if char == "X" and tracker[8] == 0 and end_loop == 0:
                        pygame.draw.line(window, white, (125,175),(175,125))
                        pygame.draw.line(window, white, (125,125),(175,175))
                        tracker.pop(8)
                        tracker.insert(8,"X")
                        game_end.append(1)
                        if len(game_end) != 9:
                            pc()
                        elif len(game_end) == 9:
                            if winner_check() == "X":
                                print("Character X won")
                            elif winner_check == "O":
                                print("Charatcer O won")
                            else:
                                print("game over")
                    if char == "O" and tracker[8] == 0 and end_loop == 0:
                        pygame.draw.circle(window, white, (150,150), 25)
                        tracker.pop(8)
                        tracker.insert(8,"O")
                        game_end.append(1)
                        if len(game_end) != 9:
                            pc()
                        elif len(game_end) == 9:
                            if winner_check() == "X":
                                print("Character X won")
                            elif winner_check == "O":
                                print("Charatcer O won")
                            else:
                                print("game over")
                    if tracker[8] != 0 and len(game_end) != 9:
                        print("slot taken try again: ")
                        human()                    
                        
        pygame.display.update()
    pygame.quit()

def pc():
    end_loop = 0
    if winner_check() == "X":
        end_loop = end_loop + 1
        print("Character X won")
    if winner_check() == "O":
        end_loop = end_loop + 1
        print("Character O won")
    pc_turn = random.randint(1,9)
    print(pc_turn)
    
    #1
    if pc_turn == 1:
        if char == "X" and tracker[0] == 0 and end_loop == 0:
            pygame.draw.circle(window, white, (50,50), 25)
            tracker.pop(0)
            tracker.insert(0,"O")
            print(tracker)
            game_end.append(1)
            if len(game_end) != 9:
                human()
            elif len(game_end) == 9:
                print("game over")
        if char == "O" and tracker[0] == 0 and end_loop == 0:
            pygame.draw.line(window, white, (25,25),(75,75))
            pygame.draw.line(window, white, (25,75),(75,25))
            tracker.pop(0)
            tracker.insert(0,"X")
            print(tracker)
            game_end.append(1)
            if len(game_end) != 9:
                human()
            elif len(game_end) == 9:
                if winner_check() == "X":
                    print("Character X won")
                elif winner_check == "O":
                    print("Charatcer O won")
                else:
                    print("game over")
        if tracker[0] != 0 and len(game_end) != 9:
            print("slot taken")
            pc()
    
    #2
    if pc_turn == 2:
        if char == "X" and tracker[1] == 0 and end_loop == 0:
            pygame.draw.circle(window, white, (100,50), 25)
            tracker.pop(1)
            tracker.insert(1,"O")
            print(tracker)
            game_end.append(1)
            if len(game_end) != 9:
                human()
            elif len(game_end) == 9:
                if winner_check() == "X":
                    print("Character X won")
                elif winner_check == "O":
                    print("Charatcer O won")
                else:
                    print("game over")
        if char == "O" and tracker[1] == 0 and end_loop == 0:
            pygame.draw.line(window, white, (75,75),(125,25))
            pygame.draw.line(window, white, (75,25),(125,75))
            tracker.pop(1)
            tracker.insert(1,"X")
            print(tracker)
            game_end.append(1)
            if len(game_end) != 9:
                human()
            elif len(game_end) == 9:
                if winner_check() == "X":
                    print("Character X won")
                elif winner_check == "O":
                    print("Charatcer O won")
                else:
                    print("game over")
        if tracker[1] != 0 and len(game_end) != 9:
            print("slot taken")
            pc()
            
    #3
    if pc_turn == 3:
        if char == "X" and tracker[2] == 0 and end_loop == 0:
            pygame.draw.circle(window, white, (150,50), 25)
            tracker.pop(2)
            tracker.insert(2,"O")
            print(tracker)
            game_end.append(1)
            if len(game_end) != 9:
                human()
            elif len(game_end) == 9:
                if winner_check() == "X":
                    print("Character X won")
                elif winner_check == "O":
                    print("Charatcer O won")
                else:
                    print("game over")
        if char == "O" and tracker[2] == 0 and end_loop == 0:
            pygame.draw.line(window, white, (125,75),(175,25))
            pygame.draw.line(window, white, (125,25),(175,75))
            tracker.pop(2)
            tracker.insert(2,"X")
            print(tracker)
            game_end.append(1)
            if len(game_end) != 9:
                human()
            elif len(game_end) == 9:
                if winner_check() == "X":
                    print("Character X won")
                elif winner_check == "O":
                    print("Charatcer O won")
                else:
                    print("game over")
        if tracker[2] != 0 and len(game_end) != 9:
            print("slot taken")
            pc()
    
    #4
    if pc_turn == 4:
        if char == "X" and tracker[3] == 0 and end_loop == 0:
            pygame.draw.circle(window, white, (50,100), 25)
            tracker.pop(3)
            tracker.insert(3,"O")
            print(tracker)
            game_end.append(1)
            if len(game_end) != 9:
                human()
            elif len(game_end) == 9:
                if winner_check() == "X":
                    print("Character X won")
                elif winner_check == "O":
                    print("Charatcer O won")
                else:
                    print("game over")
        if char == "O" and tracker[3] == 0 and end_loop == 0:
            pygame.draw.line(window, white, (25,125),(75,75))
            pygame.draw.line(window, white, (75,125),(25,75))
            tracker.pop(3)
            tracker.insert(3,"X")
            print(tracker)
            game_end.append(1)
            if len(game_end) != 9:
                human()
            elif len(game_end) == 9:
                if winner_check() == "X":
                    print("Character X won")
                elif winner_check == "O":
                    print("Charatcer O won")
                else:
                    print("game over")
        if tracker[3] != 0 and len(game_end) != 9:
            print("slot taken")
            pc()
            
    #5
    if pc_turn == 5:
        if char == "X" and tracker[4] == 0 and end_loop == 0:
            pygame.draw.circle(window, white, (100,100), 25)
            tracker.pop(4)
            tracker.insert(4,"O")
            print(tracker)
            game_end.append(1)
            if len(game_end) != 9:
                human()
            elif len(game_end) == 9:
                if winner_check() == "X":
                    print("Character X won")
                elif winner_check == "O":
                    print("Charatcer O won")
                else:
                    print("game over")
        if char == "O" and tracker[4] == 0 and end_loop == 0:
            pygame.draw.line(window, white, (75,125),(125,75))
            pygame.draw.line(window, white, (75,75),(125,125))
            tracker.pop(4)
            tracker.insert(4,"X")
            print(tracker)
            game_end.append(1)
            if len(game_end) != 9:
                human()
            elif len(game_end) == 9:
                if winner_check() == "X":
                    print("Character X won")
                elif winner_check == "O":
                    print("Charatcer O won")
                else:
                    print("game over")
        if tracker[4] != 0 and len(game_end) != 9:
            print("slot taken")
            pc()
    
    #6
    if pc_turn == 6:
        if char == "X" and tracker[5] == 0 and end_loop == 0:
            pygame.draw.circle(window, white, (150,100), 25)
            tracker.pop(5)
            tracker.insert(5,"O")
            print(tracker)
            game_end.append(1)
            if len(game_end) != 9:
                human()
            elif len(game_end) == 9:
                if winner_check() == "X":
                    print("Character X won")
                elif winner_check == "O":
                    print("Charatcer O won")
                else:
                    print("game over")
        if char == "O" and tracker[5] == 0 and end_loop == 0:
            pygame.draw.line(window, white, (125,125),(175,75))
            pygame.draw.line(window, white, (175,125),(125,75))
            tracker.pop(5)
            tracker.insert(5,"X")
            print(tracker)
            game_end.append(1)
            if len(game_end) != 9:
                human()
            elif len(game_end) == 9:
                if winner_check() == "X":
                    print("Character X won")
                elif winner_check == "O":
                    print("Charatcer O won")
                else:
                    print("game over")
        if tracker[5] != 0 and len(game_end) != 9:
            print("slot taken")
            pc()
    
    #7
    if pc_turn == 7:
        if char == "X" and tracker[6] == 0 and end_loop == 0:
            pygame.draw.circle(window, white, (50,150), 25)
            tracker.pop(6)
            tracker.insert(6,"O")
            print(tracker)
            game_end.append(1)
            if len(game_end) != 9:
                human()
            elif len(game_end) == 9:
                if winner_check() == "X":
                    print("Character X won")
                elif winner_check == "O":
                    print("Charatcer O won")
                else:
                    print("game over")
        if char == "O" and tracker[6] == 0 and end_loop == 0:
            pygame.draw.line(window, white, (75,175),(25,125))
            pygame.draw.line(window, white, (75,125),(25,175))
            tracker.pop(6)
            tracker.insert(6,"X")
            print(tracker)
            game_end.append(1)
            if len(game_end) != 9:
                human()
            elif len(game_end) == 9:
                if winner_check() == "X":
                    print("Character X won")
                elif winner_check == "O":
                    print("Charatcer O won")
                else:
                    print("game over")
        if tracker[6] != 0 and len(game_end) != 9:
            print("slot taken")
            pc()
    
    #8
    if pc_turn == 8:
        if char == "X" and tracker[7] == 0 and end_loop == 0:
            pygame.draw.circle(window, white, (100,150), 25)
            tracker.pop(7)
            tracker.insert(7,"O")
            print(tracker)
            game_end.append(1)
            if len(game_end) != 9:
                human()
            elif len(game_end) == 9:
                print("game over")
        if char == "O" and tracker[7] == 0 and end_loop == 0:
            pygame.draw.line(window, white, (75,125),(125,175))
            pygame.draw.line(window, white, (75,175),(125,125))
            tracker.pop(7)
            tracker.insert(7,"X")
            print(tracker)
            game_end.append(1)
            if len(game_end) != 9:
                human()
            elif len(game_end) == 9:
                print("game over")
        if tracker[7] != 0 and len(game_end) != 9:
            print("slot taken")
            pc()
    
    #9
    if pc_turn == 9:
        if char == "X" and tracker[8] == 0 and end_loop == 0:
            pygame.draw.circle(window, white, (150,150), 25)
            tracker.pop(8)
            tracker.insert(8,"O")
            print(tracker)
            game_end.append(1)
            if len(game_end) != 9:
                human()
            elif len(game_end) == 9:
                if winner_check() == "X":
                    print("Character X won")
                elif winner_check == "O":
                    print("Charatcer O won")
                else:
                    print("game over")
        if char == "O" and tracker[8] == 0 and end_loop == 0:
            pygame.draw.line(window, white, (125,175),(175,125))
            pygame.draw.line(window, white, (125,125),(175,175))
            tracker.pop(8)
            tracker.insert(8,"X")
            print(tracker)
            game_end.append(1)
            if len(game_end) != 9:
                human()
            elif len(game_end) == 9:
                if winner_check() == "X":
                    print("Character X won")
                elif winner_check == "O":
                    print("Charatcer O won")
                else:
                    print("game over")
        if tracker[8] != 0 and len(game_end) != 9:
            print("slot taken")
            pc()
        
def winner_check():
    if(
       tracker[0] == "X" and tracker[1] == "X" and tracker[2] == "X"
       or
       tracker[3] == "X" and tracker[4] == "X" and tracker[5] == "X"
       or
       tracker[6] == "X" and tracker[7] == "X" and tracker[8] == "X"
       or
       tracker[0] == "X" and tracker[3] == "X" and tracker[6] == "X"
       or
       tracker[1] == "X" and tracker[4] == "X" and tracker[7] == "X"
       or
       tracker[2] == "X" and tracker[5] == "X" and tracker[8] == "X"
       or
       tracker[0] == "X" and tracker[4] == "X" and tracker[8] == "X"
       or
       tracker[2] == "X" and tracker[4] == "X" and tracker[6] == "X"
       ):
        return "X"
    if(
       tracker[0] == "O" and tracker[1] == "O" and tracker[2] == "O"
       or
       tracker[3] == "O" and tracker[4] == "O" and tracker[5] == "O"
       or
       tracker[6] == "O" and tracker[7] == "O" and tracker[8] == "O"
       or
       tracker[0] == "O" and tracker[3] == "O" and tracker[6] == "O"
       or
       tracker[1] == "O" and tracker[4] == "O" and tracker[7] == "O"
       or
       tracker[2] == "O" and tracker[5] == "O" and tracker[8] == "O"
       or
       tracker[0] == "O" and tracker[4] == "O" and tracker[8] == "O"
       or
       tracker[2] == "O" and tracker[4] == "O" and tracker[6] == "O"
       ):
        return "O"
    
if turn == 1:
    human()
if turn == 2:
    pc()
