from main import destroy_walls

TestCase = tuple[list[int], list[int]]

run_cases: list[TestCase] = [
    ([0, 20, 30], [20, 30]),
    ([10, 0, 40, 0], [10, 40]),
]

submit_cases: list[TestCase] = run_cases + [
    ([], []),
    ([3, 2, 0, 3, 0, 0], [3, 2, 3]),
]


def test(wall_healths: list[int], expected: list[int]) -> bool:
    print("---------------------------------")
    print(f"Input:     {wall_healths}")
    print(f"Expected: {expected}")
    try:
        result = destroy_walls(wall_healths)
        print(f"Actual:   {result}")
        if str(result) != str(expected):
            return False
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def main() -> None:
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases: list[TestCase] = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

