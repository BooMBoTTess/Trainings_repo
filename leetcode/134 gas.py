from typing import List


class FirstSolution:

    def _next_i(self, i: int):
        if i == self.max_pos-1:
            return 0
        return i + 1


    def _step(self, pos: int, total_fuel: int , gas:  List[int], cost:  List[int]):
        total_fuel -= cost[pos]
        pos = self._next_i(pos)
        if total_fuel < 0:
            return -1, -1
        total_fuel += gas[pos]
        return total_fuel, pos
    
    def _round(self, start_pos: int, gas: List[int], cost: List[int]):
        position = start_pos
        car_fuel = gas[position]
        car_fuel, position = self._step(position, car_fuel, gas, cost)

        while position != start_pos:
            car_fuel, position = self._step(position, car_fuel, gas, cost)
            if car_fuel == -1:
                return False
        car_fuel, position = self._step(position, car_fuel, gas, cost)
        if car_fuel == -1:
            return False
        return True

    def _rm_zero_values(self, gas: List[int], cost: List[int]):
        i = 0
        counter = 0
        while i != len(gas):
            if gas[i] == 0 and cost[i] == 0:
                gas.pop(i)
                cost.pop(i)
                i -= 1
                counter += 1
            i += 1
        return gas, cost, counter

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas, cost, zero_deleted = self._rm_zero_values(gas, cost)
        self.max_pos = len(gas)
        for start in range(len(gas)):
            if self._round(start, gas, cost):
                return start + zero_deleted
        return -1


class SecondSolution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        current_gas = 0
        start = 0
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                current_gas = 0
                start = i + 1
        return start


if __name__ == '__main__':
    s = FirstSolution()
    s2 = SecondSolution()
    print(s2.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]),
    s2.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]),
    s2.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]),
    )