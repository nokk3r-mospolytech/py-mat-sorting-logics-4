//
// Created by Nokk3r on 09.06.2021.
//

#include <iostream>

void merge(int *arr, int left, int mid, int right, long long *inverses) {
    int
            len_l = mid - left + 1,
            len_r = right - mid,
            *arr_l = new int[len_l],
            *arr_r = new int[len_r];

    for (int i = 0; i < len_l; i++)
        arr_l[i] = arr[left + i];
    for (int i = 0; i < len_r; i++)
        arr_r[i] = arr[mid + 1 + i];

    int i = 0, j = 0, k = left;

    while (i < len_l && j < len_r) {
        if (arr_l[i] <= arr_r[j]) {
            arr[k] = arr_l[i];
            i++;
        } else {
            arr[k] = arr_r[j];
            j++;
            *inverses += len_l - i;
        }
        k++;
    }

    while (i < len_l) {
        arr[k] = arr_l[i];
        i++;
        k++;
    }

    while (j < len_r) {
        arr[k] = arr_r[j];
        j++;
        k++;
    }
}

void findInverses(int *arr, int left, int right, long long *inverses) {
    if (left >= right)
        return;

    int mid = left + (right - left) / 2;

    findInverses(arr, left, mid, inverses);
    findInverses(arr, mid + 1, right, inverses);

    merge(arr, left, mid, right, inverses);
}


int main() {
    int N;

    std::cin >> N;

    int *nums = new int[N];

    for (int i = 0; i < N; i++)
        std::cin >> nums[i];

    long long result = 0;

    findInverses(nums, 0, N - 1, &result);

    std::cout << result;

    return 0;
}