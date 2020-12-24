from strategy import *
from simulator import *

def main():
    sim = Simulator()

    n = 300
    for i in range(1, n):
        strategies = list()
        for j in range(0, n):
            if j <= i:
                strategies.append(TikForTat())
            else:
                strategies.append(NonCooperative())

        tik = strategies[0]
        non = strategies[-1]
        result = sim.play_round_of_robin(strategies, 30)

        if result.get_score(tik) >= result.get_score(non):
            print(f"Breakeven at {i}!")
            # print(result)
            return





    print(sim.play_round_of_robin(strategies, 30))


if __name__ == "__main__":
    main()