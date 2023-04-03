public class Main {
    public int checkOrd(int[] lst) {
            if (lst[0] < lst[lst.length - 1]) {
                return 1; // ascending order
            } else {
                return 0; // descending order
            }
        }
        public int ceilNum(int[] lst, int tar) {
            int start = 0;
            int end = lst.length - 1;
            int ch = 0;
            while (start <= end) {
                int mid = (start + end) / 2;
                if (checkOrd(lst) == 1) { // ascending order
                    if (tar > lst[mid]) {
                        start = mid + 1;
                    } else if (tar < lst[mid]) {
                        end = mid - 1;
                    } else {
                        return lst[mid];
                    }
                    ch = start;
                } else if (checkOrd(lst) == 0) { // descending order
                    if (tar < lst[mid]) {
                        start = mid + 1;
                    } else if (tar > lst[mid]) {
                        end = mid - 1;
                    } else {
                        return lst[mid];
                    }
                    ch = end;
                }
            }
            return lst[ch];
        }

        public int floor(int[] lst, int tar) {
            int start = 0;
            int end = lst.length - 1;
            int ch = 0;
            while (start <= end) {
                int mid = (start + end) / 2;
                if (checkOrd(lst) == 1) { // ascending order
                    if (tar > lst[mid]) {
                        start = mid + 1;
                    } else if (tar < lst[mid]) {
                        end = mid - 1;
                    } else {
                        return lst[mid];
                    }
                    ch = end;
                } else if (checkOrd(lst) == 0) { // descending order
                    if (tar < lst[mid]) {
                        start = mid + 1;
                    } else if (tar > lst[mid]) {
                        end = mid - 1;
                    } else {
                        return lst[mid];
                    }
                    ch = start;
                }
            }
            return lst[ch];
        }
        public static void main(String[] args) {
            //int[] lst = {-2, -1, 0, 1, 2, 9}; // array of ascending order to test
            int[] lst = {9, 2, 0, -1, -2}; // array of descending order to test
            int tar = 5;
            Main myClass = new Main();
            int sol = myClass.ceilNum(lst, tar);
            int sol2 = myClass.floor(lst, tar);
            System.out.println(sol + " " + sol2);
        }
    }
