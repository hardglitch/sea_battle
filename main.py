import random
import array


class FieldSettings:

    DIGITS: int = 0
    CHARS = array.array('u')
    RIGHTSTEPS: list = []

    @staticmethod
    def init(size: int):
        # Field size parameters. Default - 15x15
        if size in range(10, 27):
            FieldSettings.DIGITS = size
        else:
            FieldSettings.DIGITS = 15  # by default

        FieldSettings.CHARS.extend('abcdefghijklmnopqrstuvwxyz'[:FieldSettings.DIGITS])

        # ['a1', 'a2', .., 'z25', 'z26'] ─ just simple list
        for s in FieldSettings.CHARS:
            for i in range(1, FieldSettings.DIGITS + 1):
                FieldSettings.RIGHTSTEPS.append(f'{s}{i}')

        FieldSettings.RIGHTSTEPS = tuple(FieldSettings.RIGHTSTEPS)  # memory optimization


class Translate:

    LANG = array.array('u', 'eng').tounicode()
    strPlayerSideOfTheBattlefield = array.array('u', 'Your Side / CPU Steps').tounicode()
    strCPUSideOfTheBattlefield = array.array('u', 'CPU Side / Your Steps').tounicode()
    strWrongInput = array.array('u', 'It\'s a wrong input! Try again.').tounicode()
    strYourStep = array.array('u', 'Your step (Example: a1): ').tounicode()
    strYourShip = array.array('u', 'Add Your Ship:\n'
                                   '--------------------------\n'
                                   '  \'4\' - flattop x 1 (4 cells)\n'
                                   '  \'3\' - battleship x 2 (3 cells)\n'
                                   '  \'2\' - destroyer x 3 (2 cells)\n'
                                   '  \'1\' - boat x 4 (1 cells)\n'
                                   '  \'0\' - mine x 5 (1 cells)\n'
                                   '--------------------------\n'
                                   'Start Position = [a1..z26],\n'
                                   'Ship Code = [0..4],\n'
                                   'Vertical or Horizontal = [True or False] (by default - True).\n'
                                   'Examples: a1 3 True, f10 0, z20 4 False\n').tounicode()

    strShipsAreColliding = array.array('u', 'Ships are colliding.').tounicode()
    strInputFieldSize = array.array('u', 'Input the Field Size [10..26] (by default - 15): ').tounicode()
    strSelectShipsAddingMode = array.array('u', 'Select the Ships Adding Mode [automatic (1) / manually (2)]'
                                                ' (by default - automatic) : ').tounicode()
    strShipsOnFieldHelp = array.array('u', 'M - Mines, B - Boats, D - Destroyers,'
                                           ' S - Battleships, F - Flattop\n').tounicode()
    strCPUStepIs = array.array('u', 'CPU Step is').tounicode()
    strHit = array.array('u', 'Hit!').tounicode()
    strMiss = array.array('u', 'Miss.').tounicode()
    strHitToMine = array.array('u', 'Hit to Mine!').tounicode()
    strYouAreMissingStep = array.array('u', 'You are missing a Step.').tounicode()
    strCPUisMissingStep = array.array('u', 'CPU is missing a Step.').tounicode()
    strAbbreviations = array.array('u', 'MBDSF').tounicode()
    strWound = array.array('u', 'Wound!').tounicode()
    strSink = array.array('u', 'Ship has sink!').tounicode()
    strYouWon = array.array('u', 'You won!').tounicode()
    strCPUWon = array.array('u', 'CPU won!').tounicode()
    strMaxShipsOfThisType = array.array('u', 'It\'s a Maximum of this type Ships').tounicode()

    def __init__(self):
        input_message = array.array('u', 'Select Language (by default - english):\n'
                                    '- English [input \'eng\' or \'1\' or Press Enter],\n'
                                    '- Russian [input \'rus\' or \'2\']\n'
                                    '\n'
                                    'Выберите Язык (по умолчанию - английский):\n'
                                    '- Английский [введите \'eng\' или \'1\' или Нажмите Enter],\n'
                                    '- Русский [введите \'rus\' или \'2\']'
                                    '\n: ').tounicode()
        while True:
            lang: str = input(input_message).lower().strip()

            if lang in ['eng', '1', '']:
                break

            elif lang in ['rus', '2']:
                Translate.LANG = array.array('u', 'rus')
                Translate.strPlayerSideOfTheBattlefield = array.array('u', 'Ваша Сторона / Ходы Компьютера')
                Translate.strCPUSideOfTheBattlefield = array.array('u', 'Сторона Компьютера / Ваши Ходы')
                Translate.strWrongInput = array.array('u', 'Неправильный ввод. Попробуйте ещё раз.')
                Translate.strYourStep = array.array('u', 'Ваш ход (Например: a1): ')
                Translate.strYourShip = array.array('u', 'Добавте ваш корабль:\n'
                                                         '--------------------------\n'
                                                         '  \'4\' - авианосец x 1 (4 клетки)\n'
                                                         '  \'3\' - линкор x 2 (3 клетки)\n'
                                                         '  \'2\' - эсминец x 3 (2 клетки)\n'
                                                         '  \'1\' - катер x 4 (1 клетка)\n'
                                                         '  \'0\' - мина x 5 (1 клетка)\n'
                                                         '--------------------------\n'
                                                         'Начальная позиция = [a1..z26],\n'
                                                         'Код корабля = [0..4],\n'
                                                         'Вертикально или Горизонтально = [True или False]'
                                                         ' (по умолчанию - True).\n'
                                                         'Например: a1 3 True, f10 0, z20 4 False\n')

                Translate.strShipsAreColliding = array.array('u', 'Корабли накладываютя.')
                Translate.strInputFieldSize = array.array('u', 'Введите размер поля [10..26] (по умолчанию - 15): ')
                Translate.strSelectShipsAddingMode = array.array('u', 'Выберите режим добавления кораблей'
                                                                      ' [автоматически (1) / вручную (2)]'
                                                                      ' (по умолчанию - автоматически): ')
                Translate.strShipsOnFieldHelp = array.array('u', 'М - Мина, К - Катер, Э - Эсминец,'
                                                                 ' Л - Линкор, А - Авианосец\n')
                Translate.strCPUStepIs = array.array('u', 'Ход Компьютера')
                Translate.strHit = array.array('u', 'Попадание!')
                Translate.strMiss = array.array('u', 'Мимо.')
                Translate.strHitToMine = array.array('u', 'Попадание в Мину!')
                Translate.strYouAreMissingStep = array.array('u', 'Вы пропускаете ход.')
                Translate.strCPUisMissingStep = array.array('u', 'Компьютер пропускает ход.')
                Translate.strAbbreviations = array.array('u', 'МКЭЛА')
                Translate.strWound = array.array('u', 'Ранение!')
                Translate.strSink = array.array('u', 'Судно потоплено!')
                Translate.strYouWon = array.array('u', 'Вы победили!')
                Translate.strCPUWon = array.array('u', 'Компьютер победил!')
                Translate.strMaxShipsOfThisType = array.array('u', 'Это максимум судов этого типа.')
                break

            print(Translate.strWrongInput)


class Ships:  # params: size_of_ship[1..5], disposition[a1..z26], turn[vertical/horizontal]

    # ship name = '3-1' <= 3 - ship code, 1 - ship number/counter
    def __init__(self):
        self.ships: dict = {}
        self.max_ships: dict = {
            0: 5,  # mines
            1: 4,  # boats
            2: 3,  # destroyers
            3: 2,  # battleships
            4: 1,  # flattop
        }
        self.counter: dict = {
            0: 0,  # mines
            1: 0,  # boats
            2: 0,  # destroyers
            3: 0,  # battleships
            4: 0,  # flattop
        }
        self.all_ships_coordinates_list: list = []

    def all_ships_coordinates_list_maker(self):
        for ships in self.ships:
            self.all_ships_coordinates_list.extend(*[self.ships[ships]['coordinates']])
        self.all_ships_coordinates_list = list(set(self.all_ships_coordinates_list))      # deduplicate

    def add_ship(self, start_position: str, ship_code: int, vertical: bool = True) -> bool:

        if start_position in FieldSettings.RIGHTSTEPS and \
                ship_code in range(0, 5) and \
                start_position not in self.all_ships_coordinates_list:

            # temporary list for checking
            tmp = []

            if ship_code > 1:

                # 'z26' -> 'z' and '26'
                start_position_digit = int(start_position[1::])
                start_position_letter = start_position[0]

                if vertical:

                    # ship( 3, z26, vertical )
                    # z26 -> if 26+3-1 > DIGITS then start_position = 'z' + DIGITS-3+1) -> z24
                    if start_position_digit + ship_code - 1 > FieldSettings.DIGITS:
                        start_position_digit = FieldSettings.DIGITS - ship_code + 1

                    # ship coordinates - z24, z25, z26
                    for i in range(ship_code):
                        tmp.append(f'{start_position_letter}{start_position_digit+i}')
                        if self.all_ships_coordinates_list:
                            if tmp[i] in self.all_ships_coordinates_list:
                                return False

                else:

                    # horizontal
                    # ship coordinates - x26, y26, z26
                    start_index = FieldSettings.CHARS.index(start_position_letter)
                    if start_index + ship_code > FieldSettings.DIGITS:
                        start_index -= ship_code + 1

                    for i in range(ship_code):
                        tmp.append(
                            f'{FieldSettings.CHARS[start_index + i]}'
                            f'{start_position_digit}')
                        if self.all_ships_coordinates_list:
                            if tmp[i] in self.all_ships_coordinates_list:
                                return False
            else:
                tmp.append(start_position)

            # ******
            # * a1 * <- ship aura
            # * a2 *    Ship can`t be placed close to other one.
            # ******
            # ships collision check

            len_rightsteps: int = len(FieldSettings.RIGHTSTEPS)

            for i in tmp:
                try:
                    startpoint: int = FieldSettings.RIGHTSTEPS.index(i)

                    # 00**** <- letter
                    # * a1 *
                    # ******
                    index = startpoint - FieldSettings.DIGITS - 1
                    if index < 0 or startpoint % FieldSettings.DIGITS == 0:
                        index = startpoint
                    cellname = FieldSettings.RIGHTSTEPS[index]
                    if self.all_ships_coordinates_list:
                        if cellname in self.all_ships_coordinates_list:
                            return False

                    # ******
                    # 0 a1 * <- letter
                    # ******
                    index = startpoint - FieldSettings.DIGITS
                    if index <= 0:
                        index = startpoint
                    cellname = FieldSettings.RIGHTSTEPS[index]
                    if self.all_ships_coordinates_list:
                        if cellname in self.all_ships_coordinates_list:
                            return False

                    # ******
                    # * a1 *
                    # 00**** <- letter
                    index = startpoint - FieldSettings.DIGITS + 1
                    if index < 0 or index % FieldSettings.DIGITS == 0:
                        index = startpoint
                    cellname = FieldSettings.RIGHTSTEPS[index]
                    if self.all_ships_coordinates_list:
                        if cellname in self.all_ships_coordinates_list:
                            return False

                    # **00** <- letter
                    # * a1 *
                    # ******
                    index = startpoint - 1
                    if index <= 0 or startpoint % FieldSettings.DIGITS == 0:
                        index = startpoint
                    cellname = FieldSettings.RIGHTSTEPS[index]
                    if self.all_ships_coordinates_list:
                        if cellname in self.all_ships_coordinates_list:
                            return False

                    # ******
                    # * a1 * <- letter
                    # **00**
                    index = startpoint + 1
                    if index % FieldSettings.DIGITS == 0 and startpoint > 0:
                        index -= 1
                    if index >= len_rightsteps:
                        index = startpoint
                    cellname = FieldSettings.RIGHTSTEPS[index]
                    if self.all_ships_coordinates_list:
                        if cellname in self.all_ships_coordinates_list:
                            return False

                    # ****00 <- letter
                    # * a1 *
                    # ******
                    index = startpoint + FieldSettings.DIGITS - 1
                    if index >= len_rightsteps or startpoint % FieldSettings.DIGITS == 0:
                        index = startpoint
                    elif index == FieldSettings.DIGITS - 1:
                        index = startpoint + FieldSettings.DIGITS
                    cellname = FieldSettings.RIGHTSTEPS[index]
                    if self.all_ships_coordinates_list:
                        if cellname in self.all_ships_coordinates_list:
                            return False

                    # ******
                    # * a1 0 <- letter
                    # ******
                    index = startpoint + FieldSettings.DIGITS
                    if index >= len_rightsteps:
                        index = startpoint
                    cellname = FieldSettings.RIGHTSTEPS[index]
                    if self.all_ships_coordinates_list:
                        if cellname in self.all_ships_coordinates_list:
                            return False

                    # ******
                    # * a1 *
                    # ****00 <- letter
                    index = startpoint + FieldSettings.DIGITS + 1
                    if index % FieldSettings.DIGITS == 0 and startpoint > 0:
                        index = startpoint
                    if index >= len_rightsteps:
                        index = startpoint
                    cellname = FieldSettings.RIGHTSTEPS[index]
                    if self.all_ships_coordinates_list:
                        if cellname in self.all_ships_coordinates_list:
                            return False

                except True:
                    print(Translate.strShipsAreColliding)
                    return False

            if self.counter[ship_code] + 1 > self.max_ships[ship_code]:
                return False

            self.counter[ship_code] += 1

            # save ship parameters
            self.ships.update({
                f'{ship_code}-{self.counter[ship_code]}':
                {
                    'coordinates':
                    {
                        # ship coordinates and their states (Abbreviation - OK, 'X' - Killed)
                        cellname: Translate.strAbbreviations[ship_code] for cellname in tmp
                    },
                    'state': 0,   # ship state: 0 - OK, 1 - Wound, 2 - Sink.
                }
            })
            self.all_ships_coordinates_list_maker()
            return True
        else:
            return False

    def place_all_ships_automatic(self):

        def random_position() -> str:
            return random.choice(FieldSettings.RIGHTSTEPS)

        def random_vertical() -> bool:
            return random.choice([True, False])

        for shipcode in self.max_ships:
            while self.counter[shipcode] < self.max_ships[shipcode]:
                self.add_ship(random_position(), shipcode, random_vertical())


class Steps:

    # {a1, a2, .., z25, z26}
    def __init__(self):
        super().__init__()  # <= DON'T DELETE THIS !!!
        self.steps: set = set()

    def add_step(self, enemy: Ships, step: str) -> dict:

        step_result = {
            'step': False,
            'mine': False,
            'wound': False,
            'sink': False,
            'win': False,
        }
        if step in FieldSettings.RIGHTSTEPS and step not in self.steps:
            step_result['step'] = True
            self.steps.add(step)

            # hit
            if step in enemy.all_ships_coordinates_list:

                # search ship name
                shipname = ''
                for ships in enemy.ships:
                    try:
                        if enemy.ships[ships]['coordinates'][step]:
                            shipname = ships
                    except KeyError:
                        continue

                enemy.ships[shipname]['coordinates'][step] = 'X'

                # A ship is not killed
                if enemy.ships[shipname]['state'] != 2:

                    # mine: kills now, the step miss (state = 2)
                    if shipname[0] == '0':
                        enemy.ships[shipname]['state'] = 2
                        step_result['mine'] = True

                    # boat: kills now (state = 2)
                    elif shipname[0] == '1':
                        enemy.ships[shipname]['state'] = 2
                        step_result['sink'] = True

                    # destroyer, battleship or flattop
                    # The ship is wounded (state = 1)
                    elif shipname[0] in ['2', '3', '4']:
                        if enemy.ships[shipname]['state'] == 1:
                            hits = 0
                            for cells in enemy.ships[shipname]['coordinates']:
                                if enemy.ships[shipname]['coordinates'].get(cells) == 'X':
                                    hits += 1
                            if hits == int(shipname[0]):
                                enemy.ships[shipname]['state'] = 2
                                step_result['sink'] = True
                            else:
                                step_result['wound'] = True
                        else:
                            enemy.ships[shipname]['state'] = 1
                            step_result['wound'] = True

            # victory checking
            count = 0
            for shipname in enemy.ships:
                for cells in enemy.ships[shipname]['coordinates']:
                    if enemy.ships[shipname]['coordinates'].get(cells) == 'X':
                        count += 1
            if count == len(enemy.all_ships_coordinates_list):
                step_result['win'] = True

        return step_result


class PlayerInterface(Steps, Ships):

    @staticmethod
    def set_field_size():
        field_size: str = input(Translate.strInputFieldSize).strip()
        if field_size.isdigit():
            field_size: int = int(field_size)
        else:
            field_size: int = FieldSettings.DIGITS
        FieldSettings.init(field_size)

    def add_player_step(self: Steps, enemy: Ships) -> str:

        while True:
            step: str = input(Translate.strYourStep).lower().strip()
            step_result: dict = self.add_step(enemy, step)
            if step_result['step']:
                if step_result['win']:
                    print(Translate.strYouWon)
                    return 'win'
                if step_result['mine']:
                    print(f'{Translate.strHitToMine} {Translate.strYouAreMissingStep}')
                    return 'mine'
                if step_result['wound']:
                    print(Translate.strWound)
                    return 'hit'
                if step_result['sink']:
                    print(Translate.strSink)
                    return 'hit'
                print(Translate.strMiss)
                return 'miss'
            print(Translate.strWrongInput)

    def select_ships_adding_mode(self):
        #  Manually or Automatic
        mode: str = input(Translate.strSelectShipsAddingMode).strip()
        self.add_player_ship_manually() if mode == '2' else super().place_all_ships_automatic()

    def add_player_ship_manually(self: Ships):
        while True:
            #  add_player_ship( position, ship_code, vertical=True )
            Field.print_field()
            try:
                ship: list = input(Translate.strYourShip).lower().strip().split()
                for i, _ in enumerate(ship):
                    ship[i].strip()
                if len(ship) < 3:
                    ship.append('True')
                if self.add_ship(ship[0], int(ship[1]), True if ship[2] == 'True' else False):
                    if len(self.ships) == sum(self.max_ships.values()):
                        break
                    if self.counter[int(ship[1])] >= self.max_ships[int(ship[1])]:
                        print(Translate.strMaxShipsOfThisType)
                        continue
                else:
                    print(Translate.strWrongInput)
            except IndexError:
                print(Translate.strWrongInput)
                continue


class CPUInterface(Steps, Ships):

    def add_cpu_step(self, enemy: Ships) -> str:

        def cpu_logic() -> str:

            if self.steps != {}:
                for logic_step in self.steps:

                    # hits
                    if logic_step in enemy.all_ships_coordinates_list:

                        # search 'hited' ship name
                        shipname = ''
                        for ships in enemy.ships:
                            try:
                                if enemy.ships[ships]['coordinates'][logic_step]:
                                    shipname = ships
                            except KeyError or IndexError:
                                continue

                        # found wounded ship
                        if enemy.ships[shipname]['state'] != 2:

                            # attack vector (horizontal or vertical)
                            # 1. collect xcells
                            xcell = []
                            for cell in enemy.ships[shipname]['coordinates']:
                                if enemy.ships[shipname]['coordinates'].get(cell) == 'X':
                                    xcell.append(cell)

                            # 2. compare two xcells
                            horizontal_attack = False
                            vertical_attack = False
                            xcell_lenght = len(xcell)
                            if xcell_lenght > 1:
                                for i in range(xcell_lenght - 1):
                                    if xcell[i][0] != xcell[i+1][0]:
                                        horizontal_attack = True
                                        break
                                    else:
                                        vertical_attack = True
                                        break

                            len_rightsteps: int = len(FieldSettings.RIGHTSTEPS)
                            startpoint: int = FieldSettings.RIGHTSTEPS.index(logic_step)

                            if not vertical_attack:

                                # left or right
                                first: bool = random.choice([True, False])
                                for _ in range(2):
                                    if first:
                                        # left
                                        for _a in self.counter:
                                            index_left = startpoint - FieldSettings.DIGITS
                                            if index_left <= 0:
                                                index_left = startpoint
                                            cellname_left = FieldSettings.RIGHTSTEPS[index_left]
                                            if enemy.ships[shipname]['coordinates'].get(cellname_left) != 'X' and \
                                                    cellname_left not in self.steps:
                                                return cellname_left
                                    else:
                                        # right
                                        for _a in self.counter:
                                            index_right = startpoint + FieldSettings.DIGITS
                                            if index_right >= len_rightsteps:
                                                index_right = startpoint
                                            cellname_right = FieldSettings.RIGHTSTEPS[index_right]
                                            if enemy.ships[shipname]['coordinates'].get(cellname_right) != 'X' and \
                                                    cellname_right not in self.steps:
                                                return cellname_right

                                    first = not first

                            # vertical attack
                            if not horizontal_attack:

                                # up or down
                                first = random.choice([True, False])
                                for _ in range(2):
                                    if first:
                                        # up
                                        for _a in self.counter:
                                            index_up = startpoint - 1  # upper cell
                                            if index_up <= 0 or startpoint % FieldSettings.DIGITS == 0:
                                                index_up = startpoint
                                            cellname_up = FieldSettings.RIGHTSTEPS[index_up]
                                            if enemy.ships[shipname]['coordinates'].get(cellname_up) != 'X' and \
                                                    cellname_up not in self.steps:
                                                return cellname_up
                                    else:
                                        # down
                                        for _a in self.counter:
                                            index_down = startpoint + 1  # bottom cell
                                            if index_down % FieldSettings.DIGITS == 0 and startpoint > 0:
                                                index_down -= 1
                                            if index_down >= len_rightsteps:
                                                index_down = startpoint
                                            cellname_down = FieldSettings.RIGHTSTEPS[index_down]
                                            if enemy.ships[shipname]['coordinates'].get(cellname_down) != 'X' and \
                                                    cellname_down not in self.steps:
                                                return cellname_down

                                    first = not first

            return random.choice(FieldSettings.RIGHTSTEPS)

        while True:
            step: str = cpu_logic()
            step_result: dict = self.add_step(enemy, step)
            if step_result['step']:
                print(f'{Translate.strCPUStepIs} {step}. ', end='')
                if step_result['win']:
                    print(Translate.strCPUWon)
                    return 'win'
                if step_result['mine']:
                    print(f'{Translate.strHitToMine} {Translate.strCPUisMissingStep}')
                    return 'mine'
                if step_result['wound']:
                    print(Translate.strWound)
                    return 'hit'
                if step_result['sink']:
                    print(Translate.strSink)
                    return 'hit'
                print(Translate.strMiss)
                return 'miss'


class Field:

    # cell states: ' ' - space, 'X' - shot, '.' - miss

    def __init__(self, player: PlayerInterface, cpu: CPUInterface):
        self.player_side = {x: '' for x in FieldSettings.RIGHTSTEPS}
        self.cpu_side = {x: '' for x in FieldSettings.RIGHTSTEPS}
        self.player = player
        self.cpu = cpu

    def print_field(self):

        # player ships
        for ships in self.player.ships:
            for ship_coordinates in self.player.ships[ships]['coordinates']:
                self.player_side[ship_coordinates] = self.player.ships[ships]['coordinates'][ship_coordinates]

        # player steps on cpu side
        for step in self.cpu.steps:
            self.player_side[step] = 'X' if step in self.player.all_ships_coordinates_list \
                else '.'

        # cpu steps on player side
        for step in self.player.steps:
            self.cpu_side[step] = 'X' if step in self.cpu.all_ships_coordinates_list else '.'

        def switcher(cell: str) -> str:
            return ' ' if cell == '' else cell

        print(f'\n{Translate.strPlayerSideOfTheBattlefield:^{1+4*(FieldSettings.DIGITS+1)}}', ' '*5,
              f'{Translate.strCPUSideOfTheBattlefield:^{1+4*(FieldSettings.DIGITS+1)}}\n',
        
              '┌', *['───┬' for _ in range(FieldSettings.DIGITS+1)], '\b┐', ' '*5,
              '┌', *['───┬' for _ in range(FieldSettings.DIGITS+1)], '\b┐\n',
                                                               
              '│', *[f' {s} │' for s in ' '+FieldSettings.CHARS.tounicode()], ' '*5,
              '│', *[f' {s} │' for s in ' '+FieldSettings.CHARS.tounicode()], '\n',

              '│', *['───┼' for _ in range(FieldSettings.DIGITS+1)], '\b┤', ' '*5,
              '│', *['───┼' for _ in range(FieldSettings.DIGITS+1)], '\b┤',
              sep='')
        for i in range(FieldSettings.DIGITS):
            print(
              f'│{i+1:^3}│', *[f'{switcher(self.player_side[cell]):^3}│' for cell in
                               FieldSettings.RIGHTSTEPS[i::FieldSettings.DIGITS]],
              ' '*5,
              f'│{i+1:^3}│', *[f'{switcher(self.cpu_side[cell]):^3}│' for cell in
                               FieldSettings.RIGHTSTEPS[i::FieldSettings.DIGITS]],
              sep='')
            if i < FieldSettings.DIGITS-1:
                print(
                  '│', *['───┼' for _ in range(FieldSettings.DIGITS+1)], '\b┤', ' '*5,
                  '│', *['───┼' for _ in range(FieldSettings.DIGITS+1)], '\b┤',
                  sep=''
                )
        print('└', *['───┴' for _ in range(FieldSettings.DIGITS+1)], '\b┘', ' '*5,
              '└', *['───┴' for _ in range(FieldSettings.DIGITS+1)], '\b┘',
              sep='')

        print(Translate.strShipsOnFieldHelp)


# ----- Base Game -----

# --- Game Settings ---
Translate()
PlayerInterface.set_field_size()

# -- Initialisation ---
Player = PlayerInterface()
CPU = CPUInterface()
Field = Field(Player, CPU)

# --- Ships Placing ---
Player.select_ships_adding_mode()
CPU.place_all_ships_automatic()

cpu_step_result = ''
player_step_result = ''

while player_step_result != 'win' and cpu_step_result != 'win':
    Field.print_field()

    # miss one step on 'mine'
    player_step_result = Player.add_player_step(CPU) if player_step_result != 'mine' else ''

    if player_step_result == 'win':
        break
    # do yet one step on 'hit ('wound' or 'sink')'
    if player_step_result == 'hit':
        continue

    while True:
        # miss one step on 'mine'
        cpu_step_result = CPU.add_cpu_step(Player) if cpu_step_result != 'mine' else ''

        if cpu_step_result == 'win':
            break
        # do yet one step on 'hit' ('wound' or 'sink')
        if cpu_step_result != 'hit':
            break
