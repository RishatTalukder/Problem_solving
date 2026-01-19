class SegmentTree:
    def __init__(self, nums):
        """
        Build segment tree from input array
        """
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self._build(0, 0, self.n - 1, nums)

    # ---------- BUILD ----------
    def _build(self, idx, left, right, nums):
        if left == right:
            self.tree[idx] = nums[left]
            return

        mid = (left + right) // 2
        self._build(idx * 2 + 1, left, mid, nums)
        self._build(idx * 2 + 2, mid + 1, right, nums)

        self.tree[idx] = self.tree[idx * 2 + 1] + self.tree[idx * 2 + 2]

    # ---------- RANGE QUERY ----------
    def range_sum(self, ql, qr):
        return self._range_sum(0, 0, self.n - 1, ql, qr)

    def _range_sum(self, idx, left, right, ql, qr):
        if ql > right or qr < left:
            return 0

        if ql <= left and right <= qr:
            return self.tree[idx]

        self._push(idx, left, right)

        mid = (left + right) // 2
        return (
            self._range_sum(idx * 2 + 1, left, mid, ql, qr)
            + self._range_sum(idx * 2 + 2, mid + 1, right, ql, qr)
        )

    # ---------- POINT UPDATE ----------
    def point_update(self, pos, val):
        self._point_update(0, 0, self.n - 1, pos, val)

    def _point_update(self, idx, left, right, pos, val):
        if left == right:
            self.tree[idx] = val
            return

        self._push(idx, left, right)

        mid = (left + right) // 2
        if pos <= mid:
            self._point_update(idx * 2 + 1, left, mid, pos, val)
        else:
            self._point_update(idx * 2 + 2, mid + 1, right, pos, val)

        self.tree[idx] = self.tree[idx * 2 + 1] + self.tree[idx * 2 + 2]

    # ---------- RANGE UPDATE (LAZY) ----------
    def range_add(self, ql, qr, val):
        self._range_add(0, 0, self.n - 1, ql, qr, val)

    def _range_add(self, idx, left, right, ql, qr, val):
        if ql > right or qr < left:
            return

        if ql <= left and right <= qr:
            self.tree[idx] += (right - left + 1) * val
            self.lazy[idx] += val
            return

        self._push(idx, left, right)

        mid = (left + right) // 2
        self._range_add(idx * 2 + 1, left, mid, ql, qr, val)
        self._range_add(idx * 2 + 2, mid + 1, right, ql, qr, val)

        self.tree[idx] = self.tree[idx * 2 + 1] + self.tree[idx * 2 + 2]

    # ---------- LAZY PROPAGATION ----------
    def _push(self, idx, left, right):
        if self.lazy[idx] != 0:
            mid = (left + right) // 2
            val = self.lazy[idx]

            self.tree[idx * 2 + 1] += (mid - left + 1) * val
            self.tree[idx * 2 + 2] += (right - mid) * val

            self.lazy[idx * 2 + 1] += val
            self.lazy[idx * 2 + 2] += val

            self.lazy[idx] = 0
