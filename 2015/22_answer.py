class GameState:
    player_hp = None
    player_armor = None
    player_mana_avail = None
    player_mana_spent = None

    enemy_hp = None
    enemy_damage_per_turn = None

    shield_cooldown = None
    poison_cooldown = None
    recharge_cooldown = None

    winner = None

    mode = None

    def apply_shield(self):
        if self.shield_cooldown > 0:
            self.player_armor = 7
            self.shield_cooldown -= 1
        else:
            self.player_armor = 0

    def apply_poison(self):
        if self.poison_cooldown > 0:
            self.enemy_hp -= 3
            self.poison_cooldown -= 1

    def apply_recharge(self):
        if self.recharge_cooldown > 0:
            self.player_mana_avail += 101
            self.recharge_cooldown -= 1

    def apply_effects(self):
        self.apply_shield()
        self.apply_poison()
        self.apply_recharge()

    def cast_magic_missile(self):
        self.player_mana_spent += 53
        self.player_mana_avail -= 53
        self.enemy_hp -= 4

    def cast_drain(self):
        self.player_mana_spent += 73
        self.player_mana_avail -= 73
        self.enemy_hp -= 2
        self.player_hp += 2

    def cast_shield(self):
        self.player_mana_spent += 113
        self.player_mana_avail -= 113
        self.shield_cooldown = 6

    def cast_poison(self):
        self.player_mana_spent += 173
        self.player_mana_avail -= 173
        self.poison_cooldown = 6

    def cast_recharge(self):
        self.player_mana_spent += 229
        self.player_mana_avail -= 229
        self.recharge_cooldown = 5

    def cast_spell(self, spell):
        if spell == "Magic Missile":
            self.cast_magic_missile()
        elif spell == "Drain":
            self.cast_drain()
        elif spell == "Shield":
            self.cast_shield()
        elif spell == "Poison":
            self.cast_poison()
        elif spell == "Recharge":
            self.cast_recharge()

    def enemy_turn(self):
        self.apply_effects()
        if self.enemy_hp <= 0:
            self.winner = 'Player'
            return
        self.player_hp -= (self.enemy_damage_per_turn - self.player_armor)
        if self.player_hp <= 0:
            self.winner = 'Boss'
            return

    def player_turn(self, spell):
        if self.mode == "Hard":
            self.player_hp -= 1
            if self.player_hp <= 0:
                self.winner = 'Boss'
                return
        self.apply_effects()
        if self.enemy_hp <= 0:
            self.winner = 'Player'
            return
        if self.player_mana_avail < 53:
            self.winner = 'Boss'
            return
        self.cast_spell(spell)
        if self.enemy_hp <= 0:
            self.winner = 'Player'
            return

    def legal_spells(self):
        spell_list = []
        if self.player_mana_avail >= 53:
            spell_list.append("Magic Missile")
        if self.player_mana_avail >= 73:
            spell_list.append("Drain")
        if self.player_mana_avail >= 113:
            spell_list.append("Shield")
        if self.player_mana_avail >= 173:
            spell_list.append("Poison")
        if self.player_mana_avail >= 229:
            spell_list.append("Recharge")
        return spell_list

    def __init__(self, pl_hp, pl_mana, pl_arm, pl_man_sp, boss_hp, boss_dps, win, sc, pc, rc, mode):
        self.player_hp = pl_hp
        self.player_mana_avail = pl_mana
        self.player_armor = pl_arm
        self.player_mana_spent = pl_man_sp
        self.enemy_hp = boss_hp
        self.enemy_damage_per_turn = boss_dps
        self.winner = win
        self.shield_cooldown = sc
        self.poison_cooldown = pc
        self.recharge_cooldown = rc
        self.mode = mode

    def state_extract(self):
        return self.player_hp, self.player_mana_avail, self.player_armor, self.player_mana_spent, self.enemy_hp, self.enemy_damage_per_turn, self.winner, self.shield_cooldown, self.poison_cooldown, self.recharge_cooldown, self.mode

    def play_spell_chain(self, chain):
        # self.print_state()
        for spell in chain:
            if self.winner is None:
                self.player_turn(spell)
                # self.print_state()
            else:
                break
            if self.winner is None:
                self.enemy_turn()
                # self.print_state()
            else:
                break
        return self.legal_spells(), self.player_mana_spent, self.winner

    def print_state(self):
        print("Player has %d hp, %d armor, %d mana avail, %d mana spent\nBoss has %d hp\nWinner is %s" % (
            self.player_hp, self.player_armor, self.player_mana_avail, self.player_mana_spent, self.enemy_hp,
            self.winner))


in_boss_hp = 58
in_boss_damage_per_turn = 9

baseline_player_hp = 50
baseline_player_mana = 500
baseline_player_armor = 0
baseline_player_mana_spent = 0


def test_game():
    return GameState(10, 250, 0, 0, 14, 8, None, 0, 0, 0, 'Easy')


def real_game():
    return GameState(baseline_player_hp, baseline_player_mana, baseline_player_armor, baseline_player_mana_spent,
                     in_boss_hp, in_boss_damage_per_turn, None, 0, 0, 0, 'Easy')


def hard_game():
    return GameState(baseline_player_hp, baseline_player_mana, baseline_player_armor, baseline_player_mana_spent,
                     in_boss_hp, in_boss_damage_per_turn, None, 0, 0, 0, 'Hard')


def expand_active_chains(chains, min_spend):
    expansion = []
    for chain in chains:
        game = GameState(*memoize[tuple(chain[:-1])])
        legal, spent, winner = game.play_spell_chain(chain[-1:])
        memoize[tuple(chain)] = game.state_extract()
        if winner is None and spent < min_spend:
            for spell in legal:
                new_chain = chain.copy()
                new_chain.append(spell)
                expansion.append(new_chain)
        elif winner == 'Player':
            if spent < min_spend:
                min_spend = spent
    return expansion, min_spend


memoize = {tuple([]): real_game().state_extract()}
active_chains = [['Magic Missile'], ['Drain'], ['Shield'], ['Poison'], ['Recharge']]
ans_min_spend = 10000
while len(active_chains) > 0:
    active_chains, ans_min_spend = expand_active_chains(active_chains, ans_min_spend)

print('Part 1: ', ans_min_spend)

memoize = {tuple([]): hard_game().state_extract()}
active_chains = [['Magic Missile'], ['Drain'], ['Shield'], ['Poison'], ['Recharge']]
ans_min_spend = 10000
while len(active_chains) > 0:
    active_chains, ans_min_spend = expand_active_chains(active_chains, ans_min_spend)

print('Part 2: ', ans_min_spend)
