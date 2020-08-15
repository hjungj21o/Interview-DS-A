// Given a binary tree root, return the depth of the second deepest leaf.Note that if there are multiple deepest leaves, the second deepest leaf is the next highest one.

// The root has a depth of 0 and you can assume the answer is guaranteed to exist for the trees given.

// For example, given this tree, return 1 since the the second deepest leaf is 2.

// 1
// / \
// 2   3
// / \
// 4   5
// /     \
// 6       7

class Solution {
    solve(root) {
        // Write your code here
        let treeNode = { node: root, depth: 0 }
        let stack = [treeNode];
        let sett = new Set();
        while (stack.length) {
            let { node, depth } = stack.pop();

            if (!node.left && !node.right) {
                sett.add(depth);
            }

            if (node.left) {
                stack.push({ node: node.left, depth: depth + 1 })
            }
            if (node.right) {
                stack.push({ node: node.right, depth: depth + 1 })
            }
        }

        let arr = Array.from(sett).sort((a, b) => a - b);

        return arr[arr.length - 2];

    }