# DOTS Lectures 2: More Categories of Systems

## Introduction
**[00:00]**

Okay. Hello everyone. Welcome to our second lecture in the ongoing double operadic theory of systems lecture series.

We're not yet to double operads. We're still on categories. So let me review a bit of what we did last time. And this time we're just going to see, I believe, more more categories of systems and more notions more features of systems that are representable by maps between systems.

## Review of Previous Categories
**[00:52]**

So last time we saw two categories of systems. So last time we saw so one we saw discrete time time discrete space space dynamical systems - a function $U$ from $S$ to $S$ in the category of sets. Wow, that's a long phrase for just a single category. So discrete time discrete space dynamical systems. And then we saw continuous time continuous space dynamical systems. So that's two categories.

And then this map would have to be continuous, and it's perhaps much more common to see also measurable spaces. So this would be continuous space is continuous dynamics, and this one here is measurable space measurable dynamics, which is the most common one you'll see in practice. But we can also do in other categories and so I'll try and get to other interesting categories like partial maps which gives us non-determinism, and Markov kernels which gives us stochasticity.

## Continuous Time Systems and ODEs
**[05:33]**

So we also saw continuous time in the form of ODEs, and we saw that ODEs can be represented as vector fields. So an ODE is an ordinary differential equation.

## Coalgebras and System Interfaces
**[51:32]**

This leads us to coalgebras as system representations. For systems with halting states, we observe that:

- Halting states must map to halting states under morphisms
- The obvious notion of system map may not be the right notion for representability
- Proper behavior representation requires measure theory foundations

These structures are particularly valuable for:

1. Understanding systems with interfaces
2. Modeling probabilistic system behavior

## 2-Categorical Foundations of System Morphisms
**[52:45-54:50]**

### Core Framework:
1. **System 2-Category**:
   - Objects: $(S, \alpha: S \to FS)$
   - 1-cells: Homomorphisms
   - 2-cells: Simulation relations

2. **Functorial Structure**:
   For endofunctors $F,G$, a collax map consists of:
   - $\Phi: \mathbb{C} \to \mathbb{D}$
   - $\varphi: F\Phi \Rightarrow \Phi G$
   With coherence condition:
   $$\begin{CD}
   F\Phi X @>F\Phi f>> F\Phi Y \\
   @V\varphi_XVV @VV\varphi_YV \\
   \Phi GX @>>\Phi Gf> \Phi GY
   \end{CD}$$

### Key Insight:
The power set functor $\mathcal{P}$ naturally lifts to:
$$\mathcal{P}: (\mathbf{Set}, =) \to (\mathbf{Poset}, \subseteq)$$
enabling precise modeling of non-deterministic containment

## Collax Maps and Higher Category Theory
**[54:51]**

### Lyapunov Function Representation
**[55:01-55:36]**
Formally, a Lyapunov function $V: S \to \mathbb{R}^+$ satisfies:
1. $V$ is positive definite
2. $\Delta V(s) \leq 0$ along trajectories

For a system $(S, F, \alpha)$, we construct:
$$\mathcal{L}(S) = \{ V | \forall s \in S, \mathbb{E}[V(\alpha(s))] \leq V(s) \}$$

Key results:
1. Stability via categorical embeddings:
$$S \hookrightarrow \mathcal{L}(S) \hookrightarrow \mathbb{R}^+$$
2. Compositionality:
$$\mathcal{L}(S \times T) \cong \mathcal{L}(S) \otimes \mathcal{L}(T)$$havior
3. Formalizing non-deterministic mappings

The transformation cases reveal that f* u₁(s) has two distinct behaviors depending on whether u₁(s) halts or not. This demonstrates why coalgebras (F-coalgebras) provide the right framework for these system types.l equation. Okay. A vector field is we have some kind of manifold $S$, which you could think of as being $\mathbb{R}^n$, and we have its tangent bundle $\pi: TS \to S$.

The tangent bundle is roughly speaking pairs of a point $s$ paired with the tangent space at that point like this. And these are the sort of infinite decimal changes to $S$ - they're the infinite decimal changes you can make in the state.

And so a section here $u$ is a vector field, so this such that $\pi u$ equals $id_S$. In other words, we have $U(s)$ is sort of in $T_sS$. In other words, in this time, instead of saying what the next state will be, we say in our dynamics how to make an infinite decimal change in the current state.

A solution of $u$ is an actual function of time. In fact, I might write it by binding a variable in $\mathbb{R}$ just to tell you this is a function of time. So it's a function of time such that the derivative of $s$ with respect to time is equal to $u$ of $s(t)$.

Or, and then we also saw that this as well can be expressed as a map of ODEs where this is the constant one vector field. So the unit time this sort of represents the ODE:

$$\frac{d}{dt} = 1$$

## Theoretical Connections and Future Directions
**[51:40]**

Key insights from this analysis:

- The formalism excels at modeling systems with interfaces
- Representability conditions vary significantly across system types
- The 'obvious' system maps sometimes fail to preserve desired behaviors

This leads us to important conclusions about:

1. When to use coalgebraic representations
2. How measure theory enables proper behavior representation
3. Why interface systems benefit from this approach

We'll explore these concepts further in future lectures, particularly their applications to:

- Probabilistic systems
- Non-deterministic mappings
- Complex interface dependencies

## Category of Sets with a Loop
**[08:30]**

The category has one object star and all the elements of $L$ are considered as loops. So if you think of that homomorphism geometrically speaking, it takes all the points of $G$ and crushes it into a single point. You're left with a bunch of loops and you map those into each of these labels.

## Labeled Graph Homomorphisms
**[09:45]**

So now with that point of view, it's quite nice because now we can say a map of labeled graphs is a commuting square:

$$\begin{CD}
G @>>> H \\
@VVV @VVV \\
B_L @>>> B_L
\end{CD}$$

where this is $L_G$ and this is $L_H$, this is $\phi$. In other words, if we write this out, the labeling $L_H$ of $\phi(E)$ is equal to $L_G$ of $E$. In other words, a homomorphism of labeled graphs is a graph homomorphism that preserves the labelings.

## Labeled Transition Systems
**[10:15]**

So now that's a bunch of stuff like that. So what's a labeled transition system? A labeled transition system for a labeling set $L$ is a graph labeled in $L$. We think of the labels here as actions, so this is equal to a set of actions.

The idea is that the nodes of the graph, so if we have for example $G \to B_L, L_G$, the nodes of the graph $G$ are thought of as states and the edges are thought of as these transitions, ways that you can change between states. And they're labeled by the action you would have to take to do that transition. So thought of as dynamical systems, these are discrete time non-deterministic systems because there's nothing here that says that there's a unique edge out with a given label.

## Behaviors and Traces
**[11:25]**

So now with that idea, what is sort of a behavior of these, sometimes known as a trace of these LTS's? Well, it's going to be a sequence. So given a sequence of labels, or given a sequence of actions, so given a sequence $a_1 \dots a_n$ of actions in $L$, we can define a trace.

A trace for this sequence is a sequence of edges $e_1 \dots e_n$ such that when we took the action, it had that correct label. So we're taking that action on the edge and we have that correct label. And they have to line up, which means that the target of $e_i$ is equal to the source of $e_{i+1}$.

So in other words, we have some kind of graph here like $a$, $b$, $c$ or $x \dots y$ maybe some other dots here. By the way, sometimes label transition systems are called flowcharts, which is a much nicer name for them.

## Examples of Traces
**[12:15]**

For this example $L$ is equal to just one two. And so you can see if I take my sequence here to be 1111, 1112 let's say, that will give me that and then a possible edge set for that sequence would be one one one two like that. So that would be a trace.

But if instead I did 211one2, 2112, then I actually have multiple different traces for this. So I have to take this two, but then I could have multiple different traces. I could go this way and then this way and then this way, or I could go this way, this way, this way and then this way.

And so as you can see the behaviors here are sort of non-deterministic, but these are examples of traces. So maybe you can see what is going to represent this. If I put here $n$ by which I mean the graph now which has which looks like this, and I label it using $a_i$ - in other words I label the edge $a_i$ with the action $a_i$.

## Morphisms and Representability
**[13:15]**

Then a morphism like this here to here, well, it's going to send each one of these edges up top to an edge in $G$ and they have to end up because morphisms preserve source and target.

Okay, so with that point of view, it's quite nice because now we can say a map of labeled graphs is a commuting square:

$$\begin{CD}
G @>>> H \\
@VVV @VVV \\
B_L @>>> B_L
\end{CD}$$

where this is $L_G$ and this is $L_H$, this is $\phi$. In other words, if we write this out, the labeling $L_H$ of $\phi(E)$ is equal to $L_G$ of $E$. In other words, a homomorphism of labeled graphs is a graph homomorphism that preserves the labelings.
