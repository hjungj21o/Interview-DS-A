var maxDepth = function (root) {
    if (!root) return 0;
    let node = { node: root, depth: 1 };
    let stack = [node];

    let maxD = 0;

    while (stack.length) {
        let current = stack.pop();
        if (current.node.left) {
            stack.push({ node: current.node.left, depth: current.depth + 1 });
        }
        if (current.node.right) {
            stack.push({ node: current.node.right, depth: current.depth + 1 });
        }

        if (current.depth > maxD) maxD = current.depth;
    }

    return maxD

};