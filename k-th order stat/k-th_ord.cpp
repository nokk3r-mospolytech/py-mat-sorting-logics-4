//
// Created by Nokk3r on 09.06.2021.
//

#include <vector>
#include <iostream>
#include <algorithm>

std::vector<int> create_array(int p, int n, int q, int v) {
    std::vector<int> array;
    array.push_back(p);

    for (int i = 1; i < n; i++) {
        array.push_back((array[i - 1] * q) % v);
    }

    return array;
}

int partition(int* &arr, int begin, int end) {
    int piv_idx;

    piv_idx = begin;
    std::swap(arr[end - 1], arr[(begin + end - 1) / 2]);

    for (int j = begin; j < end; j++) {
        if (arr[j] < arr[end - 1]) {
            std::swap(arr[piv_idx], arr[j]);
            piv_idx++;
        }
    }

    std::swap(arr[end - 1], arr[piv_idx]);

    return piv_idx;
}

void k_th(int* &arr, int k, int n) {
    int begin = 0, end = n, pivot;

    while (true) {
        if (end - begin <= 1)
            return;

        pivot = partition(arr, begin, end);

        if (pivot == k)
            return;
        else if (k < pivot)
            end = pivot;
        else
            begin = pivot + 1;
    }
}


int main() {
//    int Q, V, P, N, K;
//    std::cin >> Q >> V >> P >> N >> K;

    int Q = 343, V = 32767, P = 3, N = 10, K = 7;

    std::vector<int> nums = create_array(P, N, Q, V);
    int* _nums = &nums[0];

    k_th(_nums, K, N);

    std::cout << _nums[K - 1];
    return 0;
}