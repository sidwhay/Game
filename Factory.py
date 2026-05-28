from Background import Background

class Factory:

  def get_entity (entity_name: str, position=(0, 0)):
        match entity_name:
            case 'bg':
                list_bg = []
                for i in range(0):
                    list_bg.append(Background(f'bg{i}', (0, 0)))
                return list_bg
       


