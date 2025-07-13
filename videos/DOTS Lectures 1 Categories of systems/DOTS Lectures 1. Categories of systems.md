# DOTS Lectures 1. Categories of systems

*Lecture by David Jaz Myers, Topos Institute*

Welcome! I'm David Jaz Myers, and this is going to be the inaugural lecture of a series on the compositional theory of systems using category theory. In particular, this is a formulation that I've come to call the **double operadic theory of systems** for reasons we'll eventually come to.

This is a way of thinking about coupled dynamical systems and how they can be presented and how their behavior can be studied using tools of category theory that we're working on jointly at the Topos Institute right now. This builds a lot on the work of the two founders of the Topos Institute, Brendan Fong and David Spivak.

This work is done with a large number of collaborators that I haven't written down on this page, but in particular, the ideas here are going to be sort of downstream of ideas of Brendan's involving **decorated cospans**, and in particular also the work of John Baez and his students on decorated and structured co-spans, and also David Spivak, Christina Vasilakopoulou, and Patrick Schultz in their paper called "Dynamical Systems and Sheaves". A lot of the ideas are going to be coming from there as well.

But I'm going to try and present a unified story that encompasses both perspectives and which gives a nice general overview of the topic that finds some commonalities between them.

There is a short extended abstract that expresses some of these ideas that I wrote for ACT 2020 or 2021. And then Sophie Libkind and I have put out a big paper getting the ball rolling on this, and we're hoping to follow this up with a number of papers putting this out. So this is sort of an introduction to this point of view on coupled systems and in particular the categorical approach to studying compositional systems.

I apologize - my nose is a little stuffy, so I may be blowing it a bit. And also, these lectures are sort of off the cuff. They're not really well prepared, so I apologize if I ever stumble or make some mistakes. I'll try to address them as quickly as possible. And namely, I apologize if I forget to name the right people or cite the right things, because I'll try to do my best, but this is something that I may forget off the top of my head.

So, with that all out of the way, I think I'm going to begin and talk about **categories of systems**. Before we're going to talk about coupled dynamical systems, I'm going to begin by talking about just the category theory of dynamical systems on its own.

## A Lightning Review of Categories

*Note: These notes are only going to really make sense to you if you already have a pretty solid background in category theory. But nevertheless, I'm going to start at the beginning and give a little talk about category theory mostly so you can just understand how I think about it and how I'm going to be using it in these lectures.*

In one sense we might say that **categories are the abstract algebra of maps or functions**.

This is a point we'll come to. So just as a vector space is an abstract algebra of vectors (and a vector is defined as something that you can take linear combinations of), a category is an abstract algebra of maps or functions, and maps are defined to be things that you can compose head to toe.

So a category consists of:

1. **Objects** - usually written in capital letters like $A$, $B$, $C$. These are things like:
   - In the category of **sets**: objects are sets
   - In the category of **groups**: objects are groups  
   - In the category of **manifolds**: objects are manifolds
   - In the category of **graphs**: objects are graphs
   - In the category of **measurable spaces**: objects are measurable spaces

2. **Maps** - For any objects $A$ and $B$ in a category $\mathcal{C}$, we have a set of arrows (maps):
   $$\mathcal{C}(A,B) = \{f : A \to B\}$$
   
   We often write $f: A \to B$ for $f \in \mathcal{C}(A,B)$.
   
   The nature of these maps depends on the category:
   - **Sets**: functions
   - **Groups**: homomorphisms (structure-preserving maps of groups)
   - **Manifolds**: We have to decide how smooth our manifolds are. If our manifold is $C^n$, then we'll take $C^n$ maps (that is, $n$ times continuously differentiable functions between them). Or we may take $C^\infty$ for smooth maps.
   - **Graphs**: graph homomorphisms
   - **Measurable spaces**: We have multiple different notions of maps. One is just **measurable functions** (functions whose inverse image preserves measurable sets). Another is **Markov kernels** - these are not understood as functions just between the measurable spaces but rather some more generalized thing, something that looks a little more like a relation.

3. **Identity maps** - For every object $A$, there's an identity map $\text{id}_A : A \to A$ that sends $x \mapsto x$.

4. **Composition** - For $f \in \mathcal{C}(A,B)$ and $g \in \mathcal{C}(B,C)$, we get $g \circ f \in \mathcal{C}(A,C)$.

The laws that govern this structure are:

- **Unity**: $f \circ \text{id}_A = f$ and $\text{id}_B \circ f = f$
- **Associativity**: $(h \circ g) \circ f = h \circ (g \circ f)$

These are easily verified for functions between sets and for that reason also between functions of these other sorts. But it is an important constraint that actually does end up constraining what can be a category. The main point is that a category is an abstract algebra of these maps, and for that reason, anything that satisfies these axioms can be a category.

I promise I'm not going to do a full introduction to categories, but I'm going to say one other thing that a category can be.

Categories - or maybe I should say **category theory**, which is a little broader than categories - is the **abstract algebra of concepts**.

A category itself is an abstract algebra of maps and it has a very precise definition. Category theory doesn't have such a precise definition like mathematics. It's best defined as that which category theorists study. But I want to define it as the abstract algebra of mathematical concepts.

What this means is - it's going to depend on what the word "concept" means - but often that means mathematical structure. What we'll see is that many concepts in mathematics can be expressed as certain mathematical structures. They can also be expressed as structures that are computed out of other structures. And we'll often see that the elements of those structures that are computed out of other structures themselves can be defined as maps of a certain kind.

So the most important thing is that **a concept - a mathematical concept - can be expressed as an arrangement of maps**.

That's sort of the fundamental idea in category theory. And because it's the abstract algebra of concepts, we're going to be able to **combine** (also known as **compose**) **concepts**. And there'll be multiple different ways we can do this, and they are determined by the above idea. We're going to determine them through **universal properties**.

This is rather vague, but that's just again this is more of a position than an actual introduction to the field.

## Fundamental Notions in Category Theory

The fundamental notions in category theory are:

1. **Universal properties**
2. **Representability** (which always means by maps)

This latter thing is essentially one of the ideas that concepts in category theory are generally represented by arrangements of maps. This is going to be really important. Both of these are going to be really important for us when we come to systems, because we'll see that systems are mathematical structures and we're going to be looking at the ways that we can study the behavior of systems. We'll see that in many cases the behaviors of systems are representable by maps between systems.

There are also other interesting things we want to understand about systems that can be represented by maps, such as coarse grains of systems, various stability properties that are proven by Lyapunov functions. Those are special kinds of structure-preserving functions of systems, and we'll come to some of those in this first lecture.

And then we'll also be combining, coupling, composing systems themselves. And we'll do that most often using techniques that are well defined by universal properties or constructions that are well defined by universal properties.

There's a sense in which universal properties and representability are special cases of each other - there's also a sense in which representability is a special case of universal properties, but that's true of every concept in category theory. Everything is everything else.

So I'm actually going to talk about **representability** first.

## Representability

Let's fix $\mathcal{C}$ to be the category of sets and functions.

Now I want to consider a concept that we can define out of a set. Given a set, we can consider its elements. 

### Representing Elements as Maps

Given a set $X$, we can represent its **elements** as maps.

How do we do that? Well, if I have an element $x \in X$, then I can make a function from some one-element set (it doesn't matter what the element of that set is). This function is defined by sending that unique element of the domain set to be the element $x$ I have.

This actually gives us a bijection:
$$X \cong \text{Hom}(\{*\}, X)$$

where $\{*\}$ is any one-element set and $\text{Hom}(\{*\}, X)$ denotes the set of functions from $\{*\}$ to $X$.

In this case we say that the **set of elements** are **representable covariantly** by this single element set. In other words, functions out of that single element set into a set correspond to elements of that set.

### Representing Pairs

Now we can also represent **pairs** of elements in $X$. We would have something like $(x_0, x_1)$ which is a pair of elements. These correspond to single functions 
$$f: \{0,1\} \to X$$
from a two-element set $\{0,1\}$, where we send $0 \mapsto x_0$ and $1 \mapsto x_1$.

So again we have that the set of pairs of elements in $X$ are bijective with the set of functions from this particular special set $\{0,1\}$ into $X$. 

This set $\{0,1\}$ is the set that just has a pair of elements in it. It is a set freely defined by a pair. We sometimes call this the **"walking pair"**, and the one-element set is the **"walking element"**.

*[The story goes that there was some category theorist who had huge bushy eyebrows and the joke was that he was just the walking pair of eyebrows. This is how that terminology arose.]*

### Representing Sequences

Similarly, **sequences** $x_0, x_1, x_2, \ldots$ (infinite sequences) correspond to maps
$$f: \mathbb{N} \to X$$
from the natural numbers into $X$.

We'll revisit this later.

I'm in danger of just giving an introduction to category theory here, so this is the sort of important idea. I'm going to sort of assume you know all of this going forward very rapidly. The main point to understand is that there are certain concepts we can express about sets that we can also represent by special sets.

## Discrete Time Dynamical Systems

So now let's consider **discrete time, discrete space dynamical systems**.

That is a very fancy way to say that such a thing is a function
$$u: S \to S$$
of sets.

We call $S$ the **set of states**, and we'll call $u$ the **dynamics** or **update function**.

The idea is that the set of states tells us how things might be, and this function $u$ takes the current way that things are and tells us the next way that things are. So these are discrete time, discrete space, deterministic dynamical systems.

### The Category of Discrete Dynamical Systems

Let's define the **category** of these things. The category of discrete time, discrete space, deterministic dynamical systems has:

**Objects**: Systems $(u: S \to S)$

**Maps**: Squares - that is, functions $f: S_0 \to S_1$ such that the following square commutes:

$$\begin{array}{ccc}
S_0 & \xrightarrow{f} & S_1 \\
\downarrow u_0 & & \downarrow u_1 \\
S_0 & \xrightarrow{f} & S_1
\end{array}$$

What does this square commuting mean? That is, for all $s_0 \in S_0$ we have the equation:
$$f(u_0(s_0)) = u_1(f(s_0))$$

In other words, if we take any state in the beginning system and we go to the next state and then we apply the function $f$, that's the same thing as first applying the function and then updating it in the target. So we say that $f$ **preserves the dynamics**.

As is the case in general in category theory, most things come down to these universally quantified equations, which are expressed by these arrangements of functions.

### Trajectories

So now let's consider an important feature of this.

**Definition**: A **trajectory** of this system is a sequence
$$s_0, s_1, s_2, \ldots$$
of states such that
$$s_{n+1} = u(s_n)$$

In other words, it's a sequence of states where each following one is defined by taking the $n$-th and applying the dynamics. This is how the system behaves - by going through such a sequence of states starting from $s_0$. 

You can also see, sort of by the principle of induction, that such a sequence of states is determined by what $s_0$ is. That's the base case, and then we have this inductive definition which just determines it.

But we'll also be able to prove a little nice theorem.

### The Trajectory Functor

The trajectory assignment gives a **functor**
$$\text{Traj}: \mathbf{Set}^{\to} \to \mathbf{Set}$$

What it means to be a functor is that if I have such a system $(u_0: S_0 \to S_0)$, then I send it to the set of trajectories of $u_0$ (defined as the set of all sequences as above). And then if I have one of these maps $f: (u_0: S_0 \to S_0) \to (u_1: S_1 \to S_1)$, this also goes to a function between the trajectory sets, and it being a functor means I get something called $\text{Traj}(f)$ which is a function that takes a trajectory of $u_0$ and gives us a trajectory of $u_1$.

What is it? Well, if I have this trajectory $(s_0, s_1, s_2, \ldots)$ of $u_0$, I just apply $f$ to each part:
$$(f(s_0), f(s_1), f(s_2), \ldots)$$

It's not obvious that this satisfies the important relation. We need to check that this is actually a trajectory. So if we take $u_1$ applied to $f(s_n)$, we need to show that that equals $f(s_{n+1})$ because that's how we define the sequence.

Well, we do know this defining property (the commuting square). So we can write:
$$u_1(f(s_n)) = f(u_0(s_n))$$
and then we can use the definition of the original sequence being a trajectory in the first place to see that $u_0(s_n) = s_{n+1}$, so:
$$f(u_0(s_n)) = f(s_{n+1})$$

And that is what we wanted. So this is what it means to be a functor - it's a homomorphism of categories.

### Representability of Trajectories

**Theorem**: The trajectory functor $\text{Traj}$ is representable by the dynamical system $(\text{succ}: \mathbb{N} \to \mathbb{N})$, where $\text{succ}(n) = n+1$.

Why? Well, as we saw, a sequence of states $(s_0, s_1, s_2, \ldots)$ corresponds to a function $s: \mathbb{N} \to S$ where $s(n) = s_n$, and the defining equation
$$s_{n+1} = u(s_n)$$
corresponds to the commuting square:

$$\begin{array}{ccc}
\mathbb{N} & \xrightarrow{s} & S \\
\downarrow \text{succ} & & \downarrow u \\
\mathbb{N} & \xrightarrow{s} & S
\end{array}$$

because this square says: for all $n \in \mathbb{N}$,
$$u(s(n)) = s(\text{succ}(n)) = s(n+1)$$

So what we've seen here is that this notion of trajectory of the system - which is a sequence of states that updates according to the law - is representable by a special simple system. In fact, to say that this is so is essentially a way of defining the natural numbers in category theory, because this is an expression of the **principle of induction**.

*[Let me blow my nose...]*

### Generalizing to Different Spaces

One thing to note is that here we've taken discrete time, discrete space, deterministic dynamical systems. They're defined like this, and we've shown that the trajectories are a sequence of states that are representable in this way. 

Now one thing I'll note is that if we wanted to change some features of this, we can change them quite slickly because, as you can see, most of this was expressed in the abstract language of category theory.

So if I wanted to say **discrete time but continuous space**, then instead of saying that it's a set here, I would say that it's a **topological space**, and all of this now takes place in the category of topological spaces and continuous functions.

Or maybe I want it to be **smooth**. Then I take the category of smooth manifolds and smooth functions.

Or maybe I just want it to be **measurable** (very common assumption in dynamical systems). And then I would take the category of measurable spaces and measurable functions.

I can do all that. But even in all those cases we can see that we can usually find the natural numbers as some kind of object and then find that discrete time trajectories are representable in this way.

So now I'm going to come to show you that representability is not just about the discrete time case but also in other things.
