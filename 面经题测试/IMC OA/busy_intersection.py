from collections import deque
FIRST_AVENUE = 1
MAIN_STREET = 0


class Solution:
    """
    @params: arrival:List[int], street:List[int]
    @return: List[int]
    """
    def get_result(self, arrival, street):
        car_quantity = len(street)
        result = [0] * car_quantity
        main_street_list = []
        first_avenue_list = []

        for i in range(car_quantity):
            if street[i] == MAIN_STREET:
                main_street_list.append((arrival[i], i))
            else:
                first_avenue_list.append((arrival[i], i))

        main_street_queue = deque(sorted(main_street_list))
        first_avenue_queue = deque(sorted(first_avenue_list))

        curr_time = 0
        prev_second = FIRST_AVENUE

        while main_street_queue or first_avenue_queue:
            if first_avenue_queue and prev_second == FIRST_AVENUE and first_avenue_queue[0][0] <= curr_time:
                _, car_id = first_avenue_queue.popleft()
                result[car_id] = curr_time
                curr_time += 1
            elif main_street_queue and prev_second == MAIN_STREET and main_street_queue[0][0] <= curr_time:
                _, car_id = main_street_queue.popleft()
                result[car_id] = curr_time
                curr_time += 1

            else:
                main_street_time = main_street_queue[0][0] if main_street_queue else float('inf')
                first_avenue_time = first_avenue_queue[0][0] if first_avenue_queue else float('inf')

                if min(main_street_time, first_avenue_time) > curr_time:
                    curr_time = min(main_street_time, first_avenue_time)
                    prev_second = FIRST_AVENUE

                if first_avenue_time <= main_street_time:
                    _, car_id = first_avenue_queue.popleft()
                    result[car_id] = curr_time
                    curr_time += 1
                    prev_second = FIRST_AVENUE
                else:
                    _, car_id = main_street_queue.popleft()
                    result[car_id] = curr_time
                    curr_time += 1
                    prev_second = MAIN_STREET

        return result


s = Solution()
arrival = [7, 9, 15, 1, 19]
street = [0, 1, 0, 1, 0]
print(s.get_result(arrival, street))  # [7, 9, 15, 1, 19]

arrival = [0, 0, 1, 4]
street = [0, 1, 1, 0]
print(s.get_result(arrival, street))  # [2, 0, 1, 4]

arrival = [0, 1, 1, 3, 3]
street = [0, 1, 0, 0, 1]
print(s.get_result(arrival, street))  # [0, 2, 1, 4, 3]
