from Background import Background
from Const import WIN_WIDTH
from Player import Player


class Factory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'bg':
                list_bg = []
                for i in range(1):
                    list_bg.append(Background(f'bg{i}', (0, 0)))

                return list_bg
            case 'Player1':
                return Player('player1', (80, WIN_WIDTH),)
            case 'Player2':
                return Player('spriteboss1', (100, WIN_WIDTH), )


        return None
