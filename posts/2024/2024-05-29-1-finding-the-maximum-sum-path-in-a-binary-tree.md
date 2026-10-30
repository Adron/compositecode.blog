---
title: Finding the Maximum Sum Path in a Binary Tree
date: 2024-05-29 22:01:00 -0700
last_modified_at: 2024-07-12 10:36:24 -0700
permalink: /2024/05/29/1-finding-the-maximum-sum-path-in-a-binary-tree/
slug: 1-finding-the-maximum-sum-path-in-a-binary-tree
wp_id: 68357
original_url: https://compositecode.blog/2024/05/29/1-finding-the-maximum-sum-path-in-a-binary-tree/
categories:
- .NET Bits
- c#
- Code Katas
tags:
- c#
- code exercises
- coding
- csharp
- dotnet
- kata
excerpt: The post delves into exploring binary tree algorithms and data structures. The author develops a Climber class to find the maximum sum path from the root to a leaf in a binary tree, accompanied by thorough testing. The code is iteratively refined, highlighting the author’s testing-centric approach and commitment to effective refactoring.
image: /wp-content/uploads/2024/05/csharp-coders.png
---

Programming Problems & Solutions: “Finding the Maximum Sum Path in a Binary Tree” is the first in this series. The introduction to this series is [here](/2024/05/29/coding-with-ai-a-comparative-series/) and includes all links to every post in the series. If you’d like to watch the video (see just below this), or the AI code up (it’s at the bottom of the post) they’re available! But if you just want to work through the problem keep reading, I cover most of what is in the video plus a slightly different path down below.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/bUUAk9_XYMU?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

*Scroll to the bottom to see the AI work through of the code base.*

Doing a little dive into the world of binary trees. If you’re in college, just got out, or having flashbacks to algorithms and data structures classes, this will be familiar territory. It’s been a hot minute since I’ve toiled through these, so figured it’d be fun to dive in again for some more modern purpose. I’m going to – over the course of the next few weeks – work through a number of algorithm and data structures problems, puzzles, katas, or what have you – and then once complete work through them with various AI tools. I’ll measure the results in whatever ways seem to bring good defining characteristics of the system and post the results. So join me, on this journey into algorithms, data structures, and a dose of AI (actually LLMs and ML but…) systems and services.

## Binary Tree & Maximum Sum Path

Imagine you’re on a journey, you have many routes to choose between, and every time you choose a route along the way you’re traversing a binary tree. Imagine each of the choices along the journey have a certain value to you, for example one part of the route versus another part of the route might have all the guitar shops or other cool things you want to stop at and see. These provide a value to each choice within the binary tree. Today, I’ll explore how to find the maximum sum path from root to leaf in a binary tree. Let’s get started!

I’ll need to setup a binary tree. Implement a function that returns the maximum sum of a route from root to leaf.

For example, given the following tree:

```
    17
   /  \
  3   -10
 /    /  \
2    16   1
         /
        13
```

My function should return `23`, since `17 -> -10 -> 16` is the route from root to leaf with the maximum sum.

If the tree is empty, return zero.

For this exercise I’ll also *not* find the best possible *route* in the tree, but instead the best possible route *from root to leaf*, e.g. for the following tree, I cannot skip the leaves and return `5 + 100 = 105`: the expected answer is `5 + 4 + -30 = -21`

```
        5
      /   \
    4      100
   / \     /
-60 -30 -120
```

Another example to proof out the idea.

```
    20
   /  \
  30   10
 /    /  \
20   16   50
    /    /
 -200  -130
```

In this case, either route going down to end in -200 or -130 will negate those routes and the chosen route would be `20 + 30 + 20 = 70`.

Ok, I’ll take a first stab at getting a tree node of sorts put together. For this class I’ll name it TreeNode and add two nested TreeNode properties to the class, as after all a binary tree has its recursive elements.

```
namespace Tree {

    public class TreeNode
    {
        public int value;
        public TreeNode left, right;

        public TreeNode(int value, TreeNode left = null, TreeNode right = null)
        {
            this.value = value;
            this.left = left;
            this.right = right;
        }

        public static TreeNode Leaf(int value)
        {
            return new TreeNode(value);
        }

        public TreeNode WithLeaves(int leftValue, int rightValue)
        {
            this.left = new TreeNode(leftValue);
            this.right = new TreeNode(rightValue);
            return this;
        }

        public TreeNode WithLeftLeaf(int leftValue)
        {
            this.left = new TreeNode(leftValue);
            return this;
        }

        public static TreeNode Join(int value, TreeNode left, TreeNode right)
        {
            return new TreeNode(value, left, right);
        }
    }
}
```

Next up, I’ll need something to provide the feature functionality

```
public class Climber
{
    public static int MaxSum(TreeNode root)
    {
        if (root == null) return 0;

        int maxSum = int.MinValue;
        FindMaxSum(root, 0, ref maxSum);
        return maxSum;
    }

    private static void FindMaxSum(TreeNode node, int currentSum, ref int maxSum)
    {
        if (node == null) return;

        currentSum += node.value;
        if (node.left == null && node.right == null)
        {
            if (currentSum > maxSum)
            {
                maxSum = currentSum;
            }
        }

        FindMaxSum(node.left, currentSum, ref maxSum);
        FindMaxSum(node.right, currentSum, ref maxSum);
    }
}
```

I did a build of what I’ve got so far and received some warnings. It’s been a while since I’ve written C# so I’m sure I’ve missed some nuance. The warnings I received didn’t seem like a big deal.

[![](/wp-content/uploads/2024/05/CleanShot-2024-05-13-at-18.46.36.png)](/wp-content/uploads/2024/05/CleanShot-2024-05-13-at-18.46.36.png)

The warnings are due to nullability issures. In C#, once I dug around a little bit in the docs, I realized with the introduction of nullable reference types the compiler enforces strict null safety to avoid null ref exceptions. Refactoring I knocked out two quick fixes.

1. Updating the `TreeNode` class to use nullable ref types for `left` and `right` properties.
2. Update the `FindMaxSum` method in the `Climber` class to check for null nodes effectively.

That wrapped that up, so onto elaboration of what I’ve just put together.

### A Break Down for the TreeNode and Its Methods

First, the `TreeNode` is our basic structure, representing each node in our binary tree.

- **Constructing a TreeNode:** You set the value and optionally connect it to other nodes, which can be either to the left or to the right.
- **Leaf Nodes:** These are nodes without children. They’re pivotal because our path will terminate on these nodes.
- **WithLeaves Method:** This method is like adding cymbals to a drum kit. It’s where a node (drummer) gets two children (cymbals), enhancing the depth and complexity of the potential paths (rhythms).
- **WithLeftLeaf Method:** Similar to adding a bass pedal to your drum setup, it adds depth to one side, enriching the texture of the music (or tree structure).
- **Join Method:** This is like forming a band by bringing together different musicians (nodes) to create a single powerful entity (a parent node with children).

### The Solution – MaxSum Method

Our `MaxSum` method is the way to find the maximum (sum).

- **Handling an Empty Tree:** If there’s no tree, there’s nothing to work with, so we simply return zero.
- **Recursive Exploration – FindMaxSum Method:**
- **Base Case:** If there’s no node just return, as there’s nothing to process.
- **Recursive Call Accumulation:** Each node adds its value to the current sum.
- **Leaf Node Check:** If we reach a leaf, we check if this was the highest. If so, we update our record.

### Detailed Walkthrough of the Recursive Process

Imagine starting at the root of the tree (the headlining song). With each recursive call, you move to the next node in the tree:

1. **Add the Current Node’s Value:** Each node’s value is added to a running total (`currentSum`).
2. **Leaf Check:** Upon reaching a leaf, if the `currentSum` is greater than the `maxSum` (the best performance so far), then we update `maxSum`.
3. **Recursive Descent:** The function then recursively calls itself for the left and right children of the current node:

- If the node has a left child, explore that path.
- Similarly, explore the right path.

Each path is explored to its fullest, down to every leaf, ensuring that every potential “song” or path is considered for its maximum “audience impact” or sum.

By the end of the recursion, `maxSum` will hold the highest sum from the root to any leaf, effectively giving us the most intense and crowd-pleasing performance of the night, measured by the sum of node values. This approach ensures that we not only explore every possible path but also capture the path that offers the maximum excitement, much like a headliner’s best performance capturing the audience’s hearts.

## Binary Tree Tests

All this, I wanted to think through the different binary tree situations and write up some tests. This is my break down using NUnit. These are all in a simple `TestFixture` class called `TreeTests`.

The first test, I just went for the easiest of all, testing for a null case.

```
    /**
     * null
     */
    [Test]
    public void MaxSumInNullTree()
    {
        TreeNode root = null;
        Assert.AreEqual(0, Climber.MaxSum(root));
    }
```

The next test I dove directly into a test case that was a little more rich. If the tree looks something like this, let’s build it out and see if we get the right result.

```
/**
 *      5
 *    /   \
 *  -22    11
 *  / \    / \
 * 9  50  9   2
 */
```

So going down each of these manually, we get `5 -22 + 9 = -8`, next `5 -22 + 50 = 33`, then `5 + 11 + 9 = 25` and last is `5 + 11 + 2 = 18`. Of those, the max is 33. So let’s put that into an assertion and see if our test passes.

```
[Test]
public void MaxSumInPerfectTree()
{
    TreeNode left = TreeNode.Leaf(-22).WithLeaves(9, 50);
    TreeNode right = TreeNode.Leaf(11).WithLeaves(9, 2);
    TreeNode root = TreeNode.Join(5, left, right);
    Assert.AreEqual(33, Climber.MaxSum(root));
}
```

Next up I tested that the processing should stop only at leaves.

```
/**
 *         5
 *       /   \
 *    4        10
 *   /  \     /
 * -143 -132 -110
 */
[Test]
public void ShouldStopOnlyAtLeaves()
{
    TreeNode left = TreeNode.Leaf(4).WithLeaves(-143, -132);
    TreeNode right = TreeNode.Leaf(10).WithLeftLeaf(-110);
    TreeNode root = TreeNode.Join(5, left, right);
    Assert.AreEqual(-51, Climber.MaxSum(root));
}
```

Next up, a right leaf and left leaf only tree.

```
/**
 *       1
 *        \
 *         2
 *          \
 *           3
 *            \
 *             4
 */
[Test]
public void MaxSumInRightSkewedTree()
{
    TreeNode root = new TreeNode(1, null, new TreeNode(2, null, new TreeNode(3, null, new TreeNode(4))));
    Assert.AreEqual(10, Climber.MaxSum(root));
}

/**
 *       1
 *      /
 *     2
 *    /
 *   3
 *  /
 * 4
 */
[Test]
public void MaxSumInLeftSkewedTree()
{
    TreeNode root = new TreeNode(1, new TreeNode(2, new TreeNode(3, new TreeNode(4))));
    Assert.AreEqual(10, Climber.MaxSum(root));
}
```

I decided then to try to get a max sum from the tree with mixed values, starting with a negative.

```
/**
 *       -10
 *      /    \
 *    9       20
 *          /   \
 *         15    7
 */
[Test]
public void MaxSumInTreeWithMixedValues()
{
    TreeNode left = TreeNode.Leaf(9);
    TreeNode right = TreeNode.Leaf(20).WithLeaves(15, 7);
    TreeNode root = TreeNode.Join(-10, left, right);
    Assert.AreEqual(25, Climber.MaxSum(root));
}
```

After that I thought, maybe zeroes might mess something out, I’ll throw something odd into tests like the following.

```
    /**
     *         0
     *       /   \
     *     1       1
     *    / \     / \
     *   0   0   0   0
     */
    [Test]
    public void MaxSumInZeroValueTree()
    {
        TreeNode left = TreeNode.Leaf(1).WithLeaves(0, 0);
        TreeNode right = TreeNode.Leaf(1).WithLeaves(0, 0);
        TreeNode root = TreeNode.Join(0, left, right);
        Assert.AreEqual(1, Climber.MaxSum(root));
    }
```

A single node tree. Will it pass?

```
/**
 *       5
 */
[Test]
public void MaxSumInSingleNodeTree()
{
    TreeNode root = new TreeNode(5);
    Assert.AreEqual(5, Climber.MaxSum(root));
}
```

The last test I went with all negatives in the tree, and figured this one probably covered all the bases to insure things are working right.

```
/**
 *          -3
 *         /   \
 *       -2    -5
 *      / \   / \
 *    -1  -4 -6  -7
 */
[Test]
public void MaxSumInAllNegativeValuesTree()
{
    TreeNode left = TreeNode.Leaf(-2).WithLeaves(-1, -4);
    TreeNode right = TreeNode.Leaf(-5).WithLeaves(-6, -7);
    TreeNode root = TreeNode.Join(-3, left, right);
    Assert.AreEqual(-6, Climber.MaxSum(root));
}
```

Running all those and I got a pass on everything.

[![](/wp-content/uploads/2024/05/CleanShot-2024-05-13-at-22.13.11.png)](/wp-content/uploads/2024/05/CleanShot-2024-05-13-at-22.13.11.png)

## Refactoring

With all those tests in place, it’s now a good time to journey back through the code base and take a stab at some refactoring. The first thing I tackled was a little work on the Climber class. First thing, I realized it could be static, so I made that change. So `public class Climber` turned into `public static class Climber`.

Next up I to `MaxSum` and realized quickly I could whittle it down from its existing state like this

```
public static int MaxSum(TreeNode root)
{
    if (root == null) return 0;

    int maxSum = int.MinValue;
    FindMaxSum(root, 0, ref maxSum);
    return maxSum;
}
```

down to a dramatically more concise single line

```
    public static int MaxSum(TreeNode root)
    {
        return root == null ? 0 : FindMaxSum(root);
    }
```

with just a little bit of refactoring of the `FindMaxSum` method.

```
private static int FindMaxSum(TreeNode? node)
{
    if (node == null) return 0;
    if (node.left == null && node.right == null) return node.value;

    int leftMaxSum = node.left != null ? FindMaxSum(node.left) : int.MinValue;
    int rightMaxSum = node.right != null ? FindMaxSum(node.right) : int.MinValue;

    return node.value + Math.Max(leftMaxSum, rightMaxSum);
}
```

Much more concise with less code to look at and read through overall. I kept thinking about it though, as the overall FindMaxSum method seemed kind of a bit much. I took a step back and decided to try answering the calls more directly per the tests, now that I’d thought it through from both points of just coding up the solution and then what outcomes should look like via tests. But I’d not written up the implementation purely from the tests, so I decided to just delete the `FindMaxSum` method and the `MaxSum` methods I had and start from the perspective of the tests first, and just implement starting from that perspective.

I started out, the first scenario is `null` which returns a max value of zero. If both the left and right children of the root are `null`, I’ve arrived at this node being a leaf node. The sum in this case is just the value of the node. I realized at this point, I could probably just write an if then else, or maybe just a switch and step through these specific cases, as there would only be a few more. These first two cases would look something like this.

```
return root switch
{
    null => 0,
    {left: null,  right: null,  value: var v} => v,
}
```

I’d then need to follow down the right side and left side. If the left child is `null` and the right child is not `null`, the sum is the value of the current node `v` plus the maximum sum from the right subtree `MaxSum(r)`. If the right child is `null` and the left child is not, the opposite of the aforementioned. The code would look like this.

```
    {left: null,  right: var r, value: var v} => v + MaxSum(r),
    {left: var l, right: null,  value: var v} => v + MaxSum(l),
```

Then the last would be the left and right children are not `null`, the sum is the value of the current node plus the max of the sums from the left and right subtrees, which ensures the path with the highest sum is chosen. Holy smokes, the final method then looks like this.

```
    public static int MaxSum(TreeNode root)
    {
        return root switch
        {
            null => 0,
            {left: null,  right: null,  value: var v} => v,
            {left: null,  right: var r, value: var v} => v + MaxSum(r),
            {left: var l, right: null,  value: var v} => v + MaxSum(l),
            {left: var l, right: var r, value: var v} => v + System.Math.Max(MaxSum(l), MaxSum(r)),
        };
    }
```

I feel like, at this point, with another pass of the tests that this is about as lean as this is going to get at this point. I’ve always found that if I kind of just hammer together a basic solution, write some tests and work through bugs that come up, then finally just delete what I had and write it based on the tests I often get an absurdly effective refactor just like this. Then of course sometimes, if my mind is working quick enough that day I just write up some tests or a harness of sorts and start from that perspective.

Either way, this binary tree is cooked for today, hope you enjoyed the post and happy coding! 🤘🏻

## Lagniappe – The AI Analysis

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/S9SolX0KfZI?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

**Reference**

- [Binary Tree](https://en.wikipedia.org/wiki/Binary_tree)
- Github: my [first draft](https://github.com/Adron/binary-tree-rambling-heavy-metal-concert/commit/e7f73da2d666efa50afccb612ffff8901cdae448) plus the [first refactoring](https://github.com/Adron/binary-tree-rambling-heavy-metal-concert/commit/296614ea7dd655dc29ec5b814c0338fe8d047061) and [second refactoring](https://github.com/Adron/binary-tree-rambling-heavy-metal-concert/commit/aa0bff436cab7aa04d8f70a81d79477c2cf52365) is available [here](https://github.com/Adron/binary-tree-rambling-heavy-metal-concert).
- Places to RTFM about syntax sugar and other details =>
  - **Pattern Matching**: This code uses pattern matching in switch expressions, which is a feature introduced in C# 8.0 and expanded in later versions. The [official Microsoft documentation on pattern matching](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/functional/pattern-matching) provides detailed explanations and examples.
  - **Switch Expressions**: The switch expression syntax is also covered under pattern matching but specifically in C# 8.0 documentation. The [documentation on switch expressions](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/switch-expression) will give you insight into how to use this feature.
  - **Records and Init-only Properties**: If you are using more advanced features like records or init-only properties with `TreeNode` class, find relevant information in the [documentation on records](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-9#record-types) and [init-only properties](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-9#init-only-setters).
  - **Static Classes and Methods**: The use of static classes and methods is well-documented in the [static classes and static class members documentation](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/static-classes-and-static-class-members).
  - **Math Methods**: For the use of `System.Math.Max`, you can refer to the [documentation on Math methods](https://learn.microsoft.com/en-us/dotnet/api/system.math.max) which describes all the mathematical functions available in the `System.Math` class.
  - **Lambda Expressions and Local Functions**: Although not directly used in your snippet, understanding lambda expressions and local functions can be beneficial for similar scenarios. The [documentation on lambda expressions](https://learn.microsoft.com/en-us/dotnet/csharp/lambda-expressions) and [local functions](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/local-functions) might be useful.
