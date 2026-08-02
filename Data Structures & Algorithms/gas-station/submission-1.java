class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length, diff[] = new int[n], totalGas = 0, totalCost = 0;
        for(int i = 0; i < n; ++i){
            diff[i] = gas[i] - cost[i];
            totalGas += gas[i];
            totalCost += cost[i];
        }

        if(totalGas < totalCost){
            return -1;
        }

        for(int i = 0; i < n; i++){
            int currGas = diff[i];
            boolean canCircuit = currGas >= 0;
            for(int j = i + 1; j < n; ++j){
                currGas += diff[j];
                if(currGas < 0){
                    canCircuit = false;
                    break;
                }
            }

            if(canCircuit){
                return i;
            }
        }
        return -1;
    }
}
