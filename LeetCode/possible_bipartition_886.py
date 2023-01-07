from collections import defaultdict


class Solution:

    def possibleBipartition(self, n, dislikes):
        NOT_COLORED, BLUE, RED = 0, 1, -1
        if n == 1 or not dislikes:
            return True

        def helper(person_id, color):
            color_table[person_id] = color

            for the_other in dislike_table[person_id]:
                if color_table[the_other] == color:
                    return False

                if color_table[the_other] == NOT_COLORED and (not helper(
                        the_other, -color)):
                    return False

            return True

        dislike_table = defaultdict(list)
        color_table = defaultdict(int)

        for p1, p2 in dislikes:
            dislike_table[p1].append(p2)
            dislike_table[p2].append(p1)
        for person_id in range(1, n + 1):
            if color_table[person_id] == NOT_COLORED and (not helper(
                    person_id, BLUE)):
                return False
        return True


if __name__ == "__main__":
    a = Solution()
    print(a.possibleBipartition(4, [[1, 2], [1, 3], [2, 4]]))
