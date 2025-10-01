#include <stddef.h>
#include <stdint.h>


double sum_row_major(const double *a, size_t rows, size_t cols) {
    double s = 0.0;
    for(size_t i = 0; i < rows; ++i) {
        const double *row = a + (i * cols);
        for(size_t j=0; j < cols; ++j) {
            s += row[j];
        }
    }

    return s;
}

double sum_col_major(const double *a, size_t rows, size_t cols) {
    double s = 0.0;
    for(size_t j=0; j<cols; ++j) {
        for(size_t i=0; i<rows; ++i) {
            s += a[(i * cols) + j];
        }
    }

    return s;
}
