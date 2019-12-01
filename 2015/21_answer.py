import itertools

weapons = ['Dagger', 'Shortsword', 'Warhammer', 'Longsword', 'Greataxe']
armors = ['No Armor', 'Leather', 'Chainmail', 'Splintmail', 'Bandedmail', 'Platemail']
rings = ['No Ring1', 'No Ring2', 'Damage +1', 'Damage +2', 'Damage +3', 'Defense +1', 'Defense +2', 'Defense +3']


class game_state:
    player_hp = 100
    player_dmg = 0
    player_arm = 0
    player_spent = 0

    enemy_hp = 103
    enemy_dmg = 9
    enemy_arm = 2

    winner = None

    equip = {
        'Dagger': (8, 4, 0),
        'Shortsword': (10, 5, 0),
        'Warhammer': (25, 6, 0),
        'Longsword': (40, 7, 0),
        'Greataxe': (74, 8, 0),
        'No Armor': (0, 0, 0),
        'Leather': (13, 0, 1),
        'Chainmail': (31, 0, 2),
        'Splintmail': (53, 0, 3),
        'Bandedmail': (75, 0, 4),
        'Platemail': (102, 0, 5),
        'No Ring1': (0, 0, 0),
        'No Ring2': (0, 0, 0),
        'Damage +1': (25, 1, 0),
        'Damage +2': (50, 2, 0),
        'Damage +3': (100, 3, 0),
        'Defense +1': (20, 0, 1),
        'Defense +2': (40, 0, 2),
        'Defense +3': (80, 0, 3),
    }

    def __init__(self, weapon, armor, ring1, ring2):
        self.player_dmg += self.equip[weapon][1]
        self.player_dmg += self.equip[ring1][1]
        self.player_dmg += self.equip[ring2][1]

        self.player_arm += self.equip[armor][2]
        self.player_arm += self.equip[ring1][2]
        self.player_arm += self.equip[ring2][2]

        self.player_spent += self.equip[weapon][0]
        self.player_spent += self.equip[armor][0]
        self.player_spent += self.equip[ring1][0]
        self.player_spent += self.equip[ring2][0]

    def play_turn(self):
        self.enemy_hp -= max(self.player_dmg - self.enemy_arm, 1)
        if self.enemy_hp <= 0:
            self.winner = 'Player'
            return
        self.player_hp -= max(self.enemy_dmg - self.player_arm, 1)
        if self.player_hp <= 0:
            self.winner = 'Enemy'
            return

    def play_game(self):
        while self.winner is None:
            self.play_turn()
        return self.winner, self.player_spent


min_spend = 10000
max_spend = 0
for weapon in weapons:
    for armor in armors:
        for ring_set in itertools.combinations(rings, 2):
            g = game_state(weapon, armor, ring_set[0], ring_set[1])
            winner, spend = g.play_game()
            if winner == 'Player':
                if spend <= min_spend:
                    min_spend = spend
            if winner == 'Enemy':
                if spend >= max_spend:
                    max_spend = spend

print('Part 1: ', min_spend)
print('Part 2: ', max_spend)
