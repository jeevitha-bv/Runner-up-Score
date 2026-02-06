if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_scores = list(set(arr))

    # Sort in descending order
    unique_scores.sort(reverse=True)

    # Print the runner-up score
    print(unique_scores[1])