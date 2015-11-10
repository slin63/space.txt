from game_tools import *

random_objects = [
    'ObjA', 'ObjB', 'ObjC', 'ObjD', 'ObjE', 'ObjF', 'ObjG', 'ObjH', 'ObjI'
]


def main(map_size, density):
    p = Player("P", 100, ["item"], C(0,0))
    s = Map(map_size, random_objects, density, player=p)
    print(len(s.get_objects()))
    while 1 == 1:
        report_surroundings(s, s.player.vision)
        esc = True
        while esc:
            ans = raw_input("Options:\n\tm - Move\n\tc - Check status\n\ti - Investigate\n\ts - Survey\n\t")
            if ans.lower() == 'm':
                direction = raw_input("Direction: ")
                magnitude = raw_input("\nDistance: ")
                d_pos = cardinal_to_dp(direction.lower(), float(magnitude))
                s.player.change_position(d_pos[0], d_pos[1])
                esc = False
            elif ans.lower() == 'c':
                print("Fuel = %s, Position = %s" % (s.player.health, s.player.position))
            elif ans.lower() == 's':
                report_surroundings(s, s.player.vision)

        # break

p = Player("P", 100, ["item"], C(0,0))
s = Map(200, random_objects, 0.05, player=p)

main(500, 0.0005)


