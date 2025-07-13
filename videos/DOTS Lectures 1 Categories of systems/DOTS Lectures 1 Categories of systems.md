# DOTS Lectures 1: Categories of Systems

## Introduction and Overview
**[0:00]**

Okay. Uh, welcome. I'm David Jazz Meyers. *[writing on board]* David Jazz Meyers.

And uh this is going to be the inaugural lecture of a series um on uh the compositional theory of systems using category theory and in particular a formulation that uh uh I've come to call the double operatic theory of systems for reasons we'll eventually come to um and this is a way of uh thinking about uh coupled dynamical systems and how they can be presented and how they their behavior can be studied um using tools of category theory uh that we're working on uh jointly at the topos institute right now and it's um so uh uh this is uh uh builds a lot uh on the work of the two founders of the topos institute Brendan Fong and David Spivak um so this is work done with a large number of collaborators that I've also haven't um haven't written down on this page but in particular um the ideas here are going to be sort of downstream of ideas uh of of Brendan's involving decorated cospans and uh and in particular also the um the work of John Baez and his students on uh decorated and structured co-spans and also David Spivak Christina Vaselopo and Patrick Schultz in this paper uh on the right um called dynamical systems and sheaves so a lot of the ideas are going to be coming from there as well. But uh I'm going to try and present a unified story that encompasses both perspectives and which uh which gives a nice um a nice sort of general overview of the of the topic that uh that that finds some commonalities between them. Um so uh there is a short extended abstract that expresses some of these ideas um that I wrote for ACT 2020 or 2021. Um so that's that first archive there on the bottom. And then the second one uh Sophie Libkind and I have put out a big uh paper um getting uh the ball rolling on this and we're hoping to uh follow this up with a number of papers uh putting this out. So this is sort of an introduction to the this point of view on coupled systems and in particular the categorical approach to studying uh compositional systems. Um, so I apologize. My nose is a little stuffy, so I may be blowing it in a bit. Um, and also, uh, these, uh, these lectures are sort of off the cuff. They're not really well prepared. Um, so I apologize if I ever stumble or make some mistakes. I'll try to address them as quick as possible. Um, and uh, and and namely, I apologize if I forget to name the right people or cite the right things. um because I'll try to do my best, but uh uh this is something that I may forget off the top of my head. So, with that all out of the way, um I think I'm going to begin uh and talk about categories of systems.

## Categories of Systems

So, before we're going to talk about coupled dynamical systems, I'm going to begin by talking about uh just the category theory of dynamical systems on its own. So, let's begin here. So, excuse me.

**[3:36]**

Okay. So, uh let's see. So, a uh uh understanding what like let's say a a lightning review of categories.

**[3:55]**

So these notes are only going to really make sense to you if you already have a pretty solid background in category theory. But nevertheless, I'm going to start at the beginning and give a little little uh talk about category theory mostly so you can just understand how I think about it and how I'm going to be using it in these lectures.

## Categories as Abstract Algebra of Maps
**[4:10]**

So in one sense we might say the categories are the abstract algebra the abstract algebras of maps or functions.

So this is a a point we'll come to. So just as a vector space is an abstract algebra of vectors and a vector is defined as something that you can take linear combinations of a category is an abstract algebra of maps or functions and maps are defined to be things that you can compose head to toe. 

So a category consists of we have some class of objects objects uh usually written in capital letters like this and these are things like eg I'll put over here eg will have the category of sets right and in that case they may be these objects may be sets in general they'll be mathematical structures though so we may have instead something like groups or we may have manifolds or we may have graphs or we may have um uh measurable spaces.

Okay. And then between those objects uh which are mathematical structures we're going to have um uh for any so this is $\mathcal{C}$ a class of objects we'll call this $\text{ob}$ in objects $A$ and $B$ in $\text{ob}$ uh uh generally a set of arrows here of these things are maps of maps maps. Um, and we often write uh a $f: A \to B$ for $f \in \mathcal{C}(A, B)$.

So now we can go through and say here are the objects, right? And then here are the maps. And so in the first case we'll have functions. Maps between sets are just functions. But in general, maps are going to have to preserve the kind of structure that the object we're going from is. So here it will be homomorphisms because a structure preserving map of groups is a homomorphism. For manifolds, we actually have to decide how how well smooth are our manifolds. So if our manifold is $C^n$, then we'll take a $C^n$ that is an $n$ times continuously differentiable functions between them. Or we may take $C^\infty$ for smooth.

Right? So depending on what kind of manifold you have, you would take that kind of map. Uh if your manifold is piecewise linear, you might for example use piecewise linear maps. There's a whole different bunch of things you could choose here. Each one of them is going to give a category. I apologize if this is uh stuff you know so well.

For graphs, there are things called graph homomorphisms and uh I'll come to those later because they're not that commonly known. Many people know what a graph is. Graphs are really central objects of study in mathematics and in computer science, but not many people express many things in terms of their homomorphisms. And um we'll talk about how a lot of concepts are represented by morphisms. 

So measurable spaces, right? We we have a multiple different notions of maps and also there's maybe again just as we had multiple different choices of maps uh for manifolds giving us multiple different categories all of whom had objects manifolds perhaps um maybe manifolds of a different kind of smoothness class whatsoever but now we can see that measurable spaces there are two sort of natural notions of map we'll see one of them is just measurable functions

So measurable functions are functions that uh that whose inverse image preserves measurable sets. But then another thing we'll see is also Markov kernels and these are uh uh these are uh uh uh not uh sort of understood as functions just between the measurable space but rather some more generalized thing something that work looks a little more like a relation. And we'll see that often categories also have the uh the uh structure that their that their morphisms or maps uh look like can look like relations between the objects, right? 

And then we have um a very special map called the identity map. Okay. And that's always the uh I guess I this is always the identity so I don't really need to write it. So is the identity and the identity map uh is is uh always the function that sends $x$ to $x$ um if you're in a functional setting and then we have composition. So for $f \in \mathcal{C}(A, B)$ and $g \in \mathcal{C}(B, C)$ we get $g \circ f \in \mathcal{C}(A, C)$ here and so this kind of composition in all this case in all these cases here is composition of maps and in this one it's actually going to be some kind of integral over the over over the kernel So it in justice is composition composition composition composition composition but uh it can be anything that satisfies sort of the uh the laws we're going to give. 

So the laws are just unity which says that $f \circ \text{id} = f$ and $\text{id} \circ f = f$ where that identity is the appropriate one. So um this is $\text{id}_A$ and this is $\text{id}_B$ and associativity $f \circ (g \circ h) = (f \circ g) \circ h$. All right. So these are easily verified for uh functions between sets and for that reason also between functions of these other sorts. Um but it is an important constraint that actually does end up constraining what can be a category. But the main point is that a category is an abstract algebra of these maps. And uh and for that reason, anything that satisfies these axioms can be a category.

## Category Theory as Abstract Algebra of Concepts
**[11:20]**

I promise I'm not going to do a full introduction to categories, but I'm going to say one other thing that a category can be. So categories or maybe I should say category theory, which is a little broader than categories, is the abstract algebra of concepts.

So a category itself is an abstract algebra of maps and it has a very precise definition. Category theory doesn't have such a precise definition like mathematics. It's best defined as that which category theorists study. But I want to define it as the abstract algebra of of mathematical concepts. And uh what this means is uh it's going to depend on what the word concept means but often that means mathematical structure. Um and uh what we'll see is that many concepts in mathematics can be expressed as certain mathematical structures. Those they can also be expressed as sort of uh uh structures that are computed out of other structures. And we'll often see that the elements of those structures that are computed out of other structures themselves can be defined as maps of a certain kind. And so this is the most thing the most important thing is that sort of a a concept can generally be defined. So um so like you know note like idea idea is that a concept that's a mathematical concept um can be expressed uh as an arrangement of maps.

That's sort of the fundamental idea in category theory. And because it's the abstract algebra of concepts, we can we're going to be able to do things. So we'll be able to able to combine combine also known as compose concepts and there'll be multiple different ways we can do this and they are determined by the above idea. We're going to determine them through um through universal properties.

All right. So this is rather vague, but that's just again this is more of a position than a than an actual introduction to the field. Uh okay, maybe I should put some introductions. We'll probably throw some introductions up in the uh up in the um description.

## Fundamental Notions in Category Theory
**[14:01]**

Okay. So, the fundamental idea, so fundamental notions in category theory.

So, uh so we're going to say one uh universal properties and two is representability ability which always means by maps. So this latter thing is essentially one of the is one of the ideas that concepts in in category theory are generally represented by arrangements of maps. And this is going to be really important. Both of these are going to be really important for us when we when we come to systems uh systems because we'll see that systems are mathematical structures and we're going to be looking at the ways that we can study the behavior of systems and we'll see that in many cases the behaviors of systems are representable by maps between systems. There also other interesting uh uh things we want to understand about systems that can be represented by maps um such as uh uh coarse grains of systems um uh various stability properties that are proven by Lyapunov functions. Those are special kinds of structure preserving functions of systems and we'll come to some of those in this in this first lecture.

Um and then we'll also be combining, coupling, composing um systems themselves. And we'll do that most often using techniques that are well defined by universal properties or constructions that are well defined by universal properties.

Okay. So uh as uh there's a sense in which that two is a special case or one is a special case of two. Um there's also a sense in which two is a special case of one, but that's that's true of every concept in category theory. Um everything is everything else. So I'm actually going to talk about representability first.

## Representability in the Category of Sets
**[16:01]**

So let's fix $\mathcal{C}$ to be the category of sets and functions.

Okay. So now I want to consider uh a a um a a concept that we can define out of a set. So given a set we can consider its elements or how about I do maybe I should do yeah I'll do I'll start with elements. So given us a set $X$, we can represent I can represent its elements as maps.

How do we do that? Well, if I have an $x \in X$, then I can make a function which I'll also well maybe for now I'll just put a little name brackets around it. A function from some one element set. It doesn't matter what the element of that set is. And this function is defined by um sending that unique element of that domain set to be the element I have. And now this is a this actually gives us a bijection. we have a bijection $X$ is bijective with the functions from this one element set to $X$.

And so in this case we say that the set of elements are representable oh covariantly by this single element set. In other words functions out of that single element set into a set correspond to elements of that set.

Now we can also represent pairs pairs um of uh elements in $X$. So we would have something like $(x_0, x_1)$ which is a pair of elements right correspond to uh pairs of functions. That's right. But they also correspond to single functions which I'll I guess I'll also write this using $X$ for the pair from a two element set now $\{0, 1\}$.

So in fact maybe doesn't get quotes maybe this one gets a little like subscript here where I send zero to $x_0$ and I send one to $x_1$.

So again we have this thing here which is that the set of pairs of elements in $X$ are bijective with the set of functions from this particular special set $\{0,1\}$ into $X$. And you can see this this this set here right is the uh the set that just has a pair of elements in it. It is a set freely defined by a pair. We sometimes call this the walking pair pair and this one's the walking element.

And I think the story goes that there was some category theorist who had huge bushy eyebrows and the joke was that uh he w he was just the walking pair of eyebrows. Um and this is how that terminology arose.

Okay. Similarly, sequences $x_0, x_1, x_2, \ldots$ infinite sequences correspond to maps $x: \mathbb{N} \to X$ from the natural numbers into $X$.

And we'll revisit this. We'll revisit this later. Okay. And I'm uh I'm at danger of just giving an introduction to category theory here. So um this is the uh this is the sort of important idea. I'm I'm going to uh sort of assume you know all of this going forward very rapidly. The main point to understand is that there are certain concepts we can express about sets that we can also represent by special sets.

So now I'll just do covariant ones. So now let's consider discrete time dynamical systems.

## Discrete Time Dynamical Systems
**[21:00]**

Discrete time discrete space dynamical systems.

That is a very very fancy way to say **def** that thing is a function:

$$u: S \to S$$

of sets. So we call $S$ the **set of states**. Let me standardize my terminology quick. And we'll call $u$ the **dynamics** or **update function**.

The idea is that the set of states tells us how things might be and this function $u$ takes the current way that things are and tells us the next way that things are. So these are discrete time discrete space deterministic dynamical systems.

### The Category of Discrete Dynamical Systems
**[22:30]**

**Definition:** The category of discrete time discrete space deterministic dynamical systems has:

- **Objects:** Systems $(S, u)$ where $u: S \to S$
- **Maps:** Functions $f: S_0 \to S_1$ such that the following square commutes:

$$\begin{CD}
S_0 @>f>> S_1 \\
@Vu_0VV @VVu_1V \\
S_0 @>>f> S_1
\end{CD}$$

What does this square commuting mean? I.e. for all $s_0 \in S_0$ we have:

$$f(u_0(s_0)) = u_1(f(s_0))$$

In other words, if we take any state in the beginning system and we go to the next state and then we apply the function $f$ that's the same thing as first applying the function and then updating it in the target. So we say that $f$ **preserves the dynamics** and as in general in category theory most things come down to these universally quantified equations which are expressed by these arrangements of functions.

### Trajectories
**[24:30]**

**Definition:** A **trajectory** of this system is a sequence:

$$s_0, s_1, s_2, \ldots$$

of states such that:

$$s_{n+1} = u(s_n)$$

In other words, it's a sequence of states where each following one is defined by taking the $n$th and applying the dynamics. This is how the system behaves by going through such a sequence of states starting from $s_0$. 

You can see by the principle of induction that such a sequence of states is determined by what $s_0$ is. That's the base case and then we have this inductive definition which determines it.

The trajectory gives a **functor** $\text{traj}: \mathbf{Set}^{\mathbf{Set}} \to \mathbf{Set}$.

What it means to be a functor is that if I have such a system $(S_0, u_0)$ then I send it to the set of trajectories of $u_0$ defined as the set of all sequences above. And if I have one of these maps $f: (S_0, u_0) \to (S_1, u_1)$ well this also goes to the trajectories and it being a functor means I get something called $\text{traj}(f)$ which is a function that takes a trajectory of $u_0$ and gives us a trajectory of $u_1$. What is it? Well if I have this trajectory of $u_0$:

$$s_0, s_1, s_2, \ldots$$

I just apply $f$ to each part:

$$f(s_0), f(s_1), f(s_2), \ldots$$

It's not obvious that this satisfies the important relation. We need to check that this is actually a trajectory. So if we take $u_1$ applied to $f(s_n)$ we need to show that equals $f(s_{n+1})$ because that's how we define the sequence. Well we know this defining property:

$$u_1(f(s_n)) = f(u_0(s_n)) = f(s_{n+1})$$

So we can pull the $f$ out and use the definition of the $s_n$s being a trajectory in the first place. This is what it means to be a functor. It's a homomorphism of categories.

## Representability of Trajectories
**[27:35]**

**Theorem:** $\text{traj}$ is representable by the dynamical system:

$$+1: \mathbb{N} \to \mathbb{N}$$

**Proof:** A sequence of states $s_0, s_1, s_2, \ldots$ corresponds to $s: \mathbb{N} \to S$ where we put the index and that defining equation:

$$s_{n+1} = u(s_n)$$

corresponds to this commutative square:

$$\begin{CD}
\mathbb{N} @>s>> S \\
@V+1VV @VVuV \\
\mathbb{N} @>>s> S
\end{CD}$$

because this square says for all $n \in \mathbb{N}$:

$$u(s(n)) = s(n+1)$$

What we've seen here is that this notion of trajectory of the system which is a sequence of states that updates according to the law is representable by a special simple system. In fact to say that this is so is essentially a way of defining the natural numbers in category theory because this is an expression of the principle of induction saying that this is determined by what $s_0$ is.

### Generalization to Other Categories
**[29:35]**

One thing to note is that we've taken discrete time discrete space deterministic dynamical systems and shown that trajectories are representable in this way. If we wanted to change some features we can change them quite slickly because most of this was expressed in the abstract language of category theory.

| Type | Category | Objects | Maps |
|------|----------|---------|------|
| Discrete time, continuous space | Topological spaces | Topological spaces | Continuous functions |
| Smooth | Manifolds | Smooth manifolds | Smooth functions |  
| Measurable | Measurable spaces | Measurable spaces | Measurable functions |

In all these cases we can usually find the natural numbers as some kind of object and find that discrete time trajectories are representable in this way.

So now I'm going to show you that representability is not just about the discrete time case but also in other things. So now we'll do systems of ODEs.

## Systems of ODEs
**[31:27]**

So a system of ODEs is pretty much the most common way to present a dynamical system in the sciences. So it's very central and so a system of ODEs is a system of differential equations of this form:

$$\begin{align}
\frac{ds_1}{dt} &= f_1(s_1, s_2, \ldots, s_n) \\
\frac{ds_2}{dt} &= f_2(s_1, s_2, \ldots, s_n) \\
&\vdots \\
\frac{ds_n}{dt} &= f_n(s_1, s_2, \ldots, s_n)
\end{align}$$

where we have $n$ state variables $s_1, \ldots, s_n$ and we set them equal to $n$ functions of themselves.

As expressed here this is an **autonomous system of ODEs**. Usually ODEs can have parameters. For now, we're not going to talk about parameterized ODEs. We'll come to that later when we talk about coupling of systems.

The thing I want you to note is we can write this as just one vector equation. If we take each $s_i \in \mathbb{R}$ and $S$ to be the whole vector, we can take $S \in \mathbb{R}^n$ and then set that equal to a whole vector equation:

$$\frac{dS}{dt} = U(S)$$

and I will never again write that little vector notation.

### Type Signature Analysis
**[16:50]**

Let's look at this and think what is the "type signature" of this. This is a function here. Simply put it's a function from $\mathbb{R}^n$ to $\mathbb{R}^n$.

But that's actually a little bit... that's true if we're just thinking about these as numbers. But it's important to note that the left hand side of this equation tells us that $U(S)$ is not really the same kind of thing as $S$ because $S$'s are **points** and these things here are **vectors** - tangent vectors in particular because the derivatives form tangent vectors.

So really we should think of it instead as we have the **tangent bundle** of $\mathbb{R}^n$ which of course is equal to $\mathbb{R}^n \times \mathbb{R}^n$:

$$\begin{CD}
T\mathbb{R}^n = \mathbb{R}^n \times \mathbb{R}^n \\
@V\pi VV \\
\mathbb{R}^n
\end{CD}$$

where these are points and these are vectors bundled over $\mathbb{R}^n$ which is the points and this here is the first projection $\pi$.

And then now we can understand what $u$ is. $U$ is a function that goes like this:

$$U: \mathbb{R}^n \to T\mathbb{R}^n$$

such that $\pi \circ U = \text{id}_{\mathbb{R}^n}$. In other words, $U$ sends $s$ to a tangent vector to $s$.

Now of course in $\mathbb{R}^n$ this is kind of overly belaboring the point. But this gives us a nice coordinate free way to write these if we have kinematical constraints.

Because if we have kinematical constraints like extra equations floating around which are not represented by the differential equations then they describe a manifold embedded in $\mathbb{R}^n$. So we might have for example $S$ here embedded in $\mathbb{R}^n$ say because:

$$S = \{s : g_1(s) = 0, g_2(s) = 0, \ldots, g_k(s) = 0\}$$

for some kinematical constraints which are expressed in terms and say the vanishing of a bunch of smooth functions.

And then the tangent bundle here really could be non-trivial. It could for example... in there is really the planes over every point $s$ it's the plane which is tangent to that point in $\mathbb{R}^n$ and so it might actually vary. For example if $S$ there was a sphere and so that's expressing a certain kinematical constraint saying that all the points we're going to... all our states are going to be points on this sphere no matter what the ODE says. We're always going to stay on the sphere and we can ensure that by saying that the ODE... that the derivatives all land tangent to the sphere always then we'll always stay on the sphere as we flow along our ODE.

So this general formulation allows us to add kinematical constraints to our system of ODEs. I'm not going to go into that, but the point is that it's going to end up being the right way to think about these systems.

### Equivalence with Vector Fields
**[18:14]**

**Definition:** A system of ODEs is equivalently a **vector field** on a smooth manifold (or on a manifold). I'm going to assume everything is smooth. That's of course not necessary to assume, but I'm not going to get bogged down in analytical details here.

What is that? Well, we have a manifold $S$ with its tangent bundle and then we have $U$ which is a **section of the bundle**:

$$U: S \to TS$$

where $\pi \circ U = \text{id}_S$.

And again the actual differential equation itself - the ODE itself - is:

$$\frac{dS}{dt} = U(S)$$

### Morphisms of ODEs
**[19:19]**

**Definition:** A **morphism** (a map of ODEs). If you're a category theorist, you'll know what I mean when I say it's a map such that the obvious squares commute. This is one of the fun things about category theory is knowing after a little while what it means. If you give a definition of an object, it usually implicitly comes with a definition of the morphism by sort of letting everything in that definition vary according to its natural variance.

In this case, we're going to say that it's a map $f: S \to S_1$ that makes the following diagram commute, which will look in a way a lot like the one we saw in the discrete time case:

$$\begin{CD}
TS @>TF>> TS_1 \\
@VUVV @VVU_1V \\
S @>>F> S_1
\end{CD}$$

Technically we should also add the "obvious diagram" that this commutes with the $\pi$, but that follows for free, so we don't need to add it.

And $TF$ here is the **pushforward** of vectors. What does that mean for $\mathbb{R}^n$s which we're really thinking about? Well, in the $\mathbb{R}^n$ case we have $\mathbb{R}^n \times \mathbb{R}^n$ and then maybe $\mathbb{R}^m \times \mathbb{R}^m$:

$$\begin{CD}
\mathbb{R}^n \times \mathbb{R}^n @>TF>> \mathbb{R}^m \times \mathbb{R}^m \\
@V\pi VV @VV\pi V \\
\mathbb{R}^n @>>F> \mathbb{R}^m
\end{CD}$$

We have $\mathbb{R}^n$, we have $\mathbb{R}^m$ and we have $F$ here. And then here we're going to take a point $p$ and a vector $v$ and we're going to give a point and a vector and that point here is going to be $F(p)$. But then what we're going to give is the directional derivative in the direction of $v$ of $F$ at $p$:

$$TF(p,v) = (F(p), D_v F|_p)$$

So this is what $TF$ is. And so that's going to be our definition of map. $T$ is another example of a functor and this is how it acts on maps.

### Trajectories of ODEs
**[39:59]**

So now we'll see that a **trajectory** is going to be a **curve**, or let me just call it a **solution** to the ODE.

If you look at the ODE, remember that it expressed this equation:

$$\frac{dS}{dt} = U(S)$$

The $U$ expressed this equation and that equation has something kind of important in it which is it has this $t$ which was unexplained.

So what a solution is, if we are careful about it, is it's an $s$ which is a function - at least differentiable function from $\mathbb{R}$ to $S$ where we think of it as a function of the variable $t$:

$$s(t)$$

such that the function actually satisfies this equation for all times $t$:

$$\frac{ds}{dt}(t) = U(s(t))$$

## Representability of ODE Trajectories
**[41:11]**

And so now we'll come to our theorem here which is that **trajectories of ODEs are representable by the single ODE**:

$$\frac{dt}{dt} = 1$$

Time flows at unit rate, which is actually the ODE with constant $1$. Or really, because this is equal to $\mathbb{R} \times \mathbb{R}$, this is:

$$t \mapsto (t, 1)$$

So maps from that into $S$ are going to be precisely that equation up there. So again we see that the notion of solution to an ODE is representable.

## Conclusion
**[42:02]**

And we'll pick this up next time, seeing more examples of representability before eventually coming to consider the coupling and composition of systems.
