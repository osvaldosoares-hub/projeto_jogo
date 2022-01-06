import pygame
import pytest

from main import Game
from states.menu_state import Menu
from states.play_state_one import Play_stage_one
from states.play_state_two import Play_stage_two
  

game = Game()
menu = Menu(game)
stage_one = Play_stage_one(game)
stage_two = Play_stage_two(game)

pygame.display.quit()
pygame.quit()



def test_controls_rigth():

    valid_to_start = game.actions['right']
    assert valid_to_start == False

def test_controls_left():

    valid_to_start = game.actions['left']
    assert valid_to_start == False

def test_controls_shot():

    valid_to_start = game.actions['action1']
    assert valid_to_start == False

def test_controls_jump_to_next():

    valid_to_start = game.actions['action2']
    assert valid_to_start == False

def test_start():
    
    run = game.runing 
    assert run == True

def test_play():

    play = game.playing
    
    assert play  == True

def test_delta_type():
    game.get_dt()
    test_type = game.dt

    assert type(test_type) == type(1.0)

def test_prev_time_type():

    game.get_dt()
    test_type = game.prev_time
    assert type(test_type) == type(1.0)

def test_initial_waiting():

    test_waiting = menu.waiting

    assert test_waiting == True

def test_create_enemies_stage_one():
    
    create = stage_one.create

    assert create == True

def test_create_enemies_stage_two():
    
    create = stage_two.create

    assert create == True







