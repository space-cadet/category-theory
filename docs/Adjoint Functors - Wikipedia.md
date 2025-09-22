---
category:
  - "[[Clippings]]"
author: 
title: Adjoint functors - Wikipedia
source: https://en.wikipedia.org/wiki/Adjoint_functors
clipped: 2024-10-13
published: 
topics: 
tags:
  - clippings
  - category-theory
  - wikipedia
---

In [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), specifically [category theory](https://en.wikipedia.org/wiki/Category_theory "Category theory"), **adjunction** is a relationship that two [functors](https://en.wikipedia.org/wiki/Functor "Functor") may exhibit, intuitively corresponding to a weak form of equivalence between two related categories. Two functors that stand in this relationship are known as **adjoint functors**, one being the **left adjoint** and the other the **right adjoint**. Pairs of adjoint functors are ubiquitous in mathematics and often arise from constructions of "optimal solutions" to certain problems (i.e., constructions of objects having a certain [universal property](https://en.wikipedia.org/wiki/Universal_property "Universal property")), such as the construction of a [free group on a set](https://en.wikipedia.org/wiki/Free_group "Free group") in algebra, or the construction of the [Stone–Čech compactification](https://en.wikipedia.org/wiki/Stone%E2%80%93%C4%8Cech_compactification "Stone–Čech compactification") of a [topological space](https://en.wikipedia.org/wiki/Topological_space "Topological space") in topology.

By definition, an adjunction between categories ![{\displaystyle {\mathcal {C}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e7b3edab7022ca9e2976651bc59c489513ee9019) and ![{\displaystyle {\mathcal {D}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/3277962e1959c3241fb1b70c7f0ac6dcefebd966) is a pair of functors (assumed to be [covariant](https://en.wikipedia.org/wiki/Covariant_functor "Covariant functor"))

![{\displaystyle F:{\mathcal {D}}\rightarrow {\mathcal {C}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f69dd2f208399a25c9a8c3c60a3306ab1b74fb4a)   and   ![{\displaystyle G:{\mathcal {C}}\rightarrow {\mathcal {D}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ad4383e5ace52ee145e777c803a0a47dd138b049)

and, for all objects ![{\displaystyle X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/68baa052181f707c662844a465bfeeb135e82bab) in ![{\displaystyle {\mathcal {C}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e7b3edab7022ca9e2976651bc59c489513ee9019) and ![{\displaystyle Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/961d67d6b454b4df2301ac571808a3538b3a6d3f) in ![{\displaystyle {\mathcal {D}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/3277962e1959c3241fb1b70c7f0ac6dcefebd966), a [bijection](https://en.wikipedia.org/wiki/Bijection "Bijection") between the respective morphism sets

![{\displaystyle \mathrm {hom} _{\mathcal {C}}(FY,X)\cong \mathrm {hom} _{\mathcal {D}}(Y,GX)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/41c5faa5f9e762dd4c453b1af3e59be494bd630a)

such that this family of bijections is [natural](https://en.wikipedia.org/wiki/Natural_transformation "Natural transformation") in ![{\displaystyle X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/68baa052181f707c662844a465bfeeb135e82bab) and ![{\displaystyle Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/961d67d6b454b4df2301ac571808a3538b3a6d3f). Naturality here means that there are natural isomorphisms between the pair of functors ![{\displaystyle {\mathcal {C}}(F-,X):{\mathcal {D}}\to \mathrm {Set^{\text{op}}} }](https://wikimedia.org/api/rest_v1/media/math/render/svg/d745a9fc9436e5929bb3600c8e7fef8b888bba72) and ![{\displaystyle {\mathcal {D}}(-,GX):{\mathcal {D}}\to \mathrm {Set^{\text{op}}} }](https://wikimedia.org/api/rest_v1/media/math/render/svg/48490737bdc397460627fecfb44ea3aaeb702d3e) for a fixed ![{\displaystyle X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/68baa052181f707c662844a465bfeeb135e82bab) in ![{\displaystyle {\mathcal {C}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e7b3edab7022ca9e2976651bc59c489513ee9019), and also the pair of functors ![{\displaystyle {\mathcal {C}}(FY,-):{\mathcal {C}}\to \mathrm {Set} }](https://wikimedia.org/api/rest_v1/media/math/render/svg/d36c5cfa1b9ddac208c26c5619f5d3eb5eabedc7) and ![{\displaystyle {\mathcal {D}}(Y,G-):{\mathcal {C}}\to \mathrm {Set} }](https://wikimedia.org/api/rest_v1/media/math/render/svg/38306b4b0f78cd0da109c27d7ba1d93adc83e3c4) for a fixed ![{\displaystyle Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/961d67d6b454b4df2301ac571808a3538b3a6d3f) in ![{\displaystyle {\mathcal {D}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/3277962e1959c3241fb1b70c7f0ac6dcefebd966).

The functor ![{\displaystyle F}](https://wikimedia.org/api/rest_v1/media/math/render/svg/545fd099af8541605f7ee55f08225526be88ce57) is called a **left adjoint functor** or **left adjoint to ![{\displaystyle G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f5f3c8921a3b352de45446a6789b104458c9f90b)** , while ![{\displaystyle G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f5f3c8921a3b352de45446a6789b104458c9f90b) is called a **right adjoint functor** or **right adjoint to ![{\displaystyle F}](https://wikimedia.org/api/rest_v1/media/math/render/svg/545fd099af8541605f7ee55f08225526be88ce57)** . We write ![{\displaystyle F\dashv G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/721042515894e125efb15c7811026d9941bb55f2).

An adjunction between categories ![{\displaystyle {\mathcal {C}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e7b3edab7022ca9e2976651bc59c489513ee9019) and ![{\displaystyle {\mathcal {D}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/3277962e1959c3241fb1b70c7f0ac6dcefebd966) is somewhat akin to a "weak form" of an [equivalence](https://en.wikipedia.org/wiki/Equivalence_of_categories "Equivalence of categories") between ![{\displaystyle {\mathcal {C}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e7b3edab7022ca9e2976651bc59c489513ee9019) and ![{\displaystyle {\mathcal {D}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/3277962e1959c3241fb1b70c7f0ac6dcefebd966), and indeed every equivalence is an adjunction. In many situations, an adjunction can be "upgraded" to an equivalence, by a suitable natural modification of the involved categories and functors.

## Terminology and notation

\[[edit](https://en.wikipedia.org/w/index.php?title=Adjoint_functors&action=edit&section=1 "Edit section: Terminology and notation")\]

The terms *[adjoint](https://en.wiktionary.org/wiki/adjoint "wikt:adjoint")* and *[adjunct](https://en.wiktionary.org/wiki/adjunct "wikt:adjunct")* are both used, and are [cognates](https://en.wikipedia.org/wiki/Cognate "Cognate"): one is taken directly from Latin, the other from Latin via French. In the classic text *Categories for the Working Mathematician*, [Mac Lane](https://en.wikipedia.org/wiki/Saunders_Mac_Lane "Saunders Mac Lane") makes a distinction between the two. Given a family

![{\displaystyle \varphi _{XY}:\mathrm {hom} _{\mathcal {C}}(FY,X)\cong \mathrm {hom} _{\mathcal {D}}(Y,GX)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/bbdf761692167153b3ccc12c9d3fccb3b78ebc6a)

of hom-set bijections, we call ![{\displaystyle \varphi }](https://wikimedia.org/api/rest_v1/media/math/render/svg/33ee699558d09cf9d653f6351f9fda0b2f4aaa3e) an **adjunction** or an **adjunction between ![{\displaystyle F}](https://wikimedia.org/api/rest_v1/media/math/render/svg/545fd099af8541605f7ee55f08225526be88ce57) and ![{\displaystyle G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f5f3c8921a3b352de45446a6789b104458c9f90b)** . If ![{\displaystyle f}](https://wikimedia.org/api/rest_v1/media/math/render/svg/132e57acb643253e7810ee9702d9581f159a1c61) is an arrow in ![{\displaystyle \mathrm {hom} _{\mathcal {C}}(FY,X)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0c0f17f2f21052d8bc1011ed96920c3c7627147c), ![{\displaystyle \varphi f}](https://wikimedia.org/api/rest_v1/media/math/render/svg/374b529113a38c5ccca9b89a82d2e99ff04a9f3d) is the right **adjunct** of ![{\displaystyle f}](https://wikimedia.org/api/rest_v1/media/math/render/svg/132e57acb643253e7810ee9702d9581f159a1c61) (p. 81). The functor ![{\displaystyle F}](https://wikimedia.org/api/rest_v1/media/math/render/svg/545fd099af8541605f7ee55f08225526be88ce57) is **left adjoint** to ![{\displaystyle G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f5f3c8921a3b352de45446a6789b104458c9f90b), and ![{\displaystyle G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f5f3c8921a3b352de45446a6789b104458c9f90b) is **right adjoint** to ![{\displaystyle F}](https://wikimedia.org/api/rest_v1/media/math/render/svg/545fd099af8541605f7ee55f08225526be88ce57). (Note that ![{\displaystyle G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f5f3c8921a3b352de45446a6789b104458c9f90b) may have itself a right adjoint that is quite different from ![{\displaystyle F}](https://wikimedia.org/api/rest_v1/media/math/render/svg/545fd099af8541605f7ee55f08225526be88ce57); see below for an example.)

In general, the phrases "![{\displaystyle F}](https://wikimedia.org/api/rest_v1/media/math/render/svg/545fd099af8541605f7ee55f08225526be88ce57) is a left adjoint" and "![{\displaystyle F}](https://wikimedia.org/api/rest_v1/media/math/render/svg/545fd099af8541605f7ee55f08225526be88ce57) has a right adjoint" are equivalent. We call ![{\displaystyle F}](https://wikimedia.org/api/rest_v1/media/math/render/svg/545fd099af8541605f7ee55f08225526be88ce57) a left adjoint because it is applied to the left argument of ![{\displaystyle \mathrm {hom} _{\mathcal {C}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f2ae69c0bc0562bd1f119f7d0b3f8980eee999c3), and ![{\displaystyle G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f5f3c8921a3b352de45446a6789b104458c9f90b) a right adjoint because it is applied to the right argument of ![{\displaystyle \mathrm {hom} _{\mathcal {D}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2cd5f206f0ea58f667d2c2300655b0adaacc28b8).

If *F* is left adjoint to *G*, we also write

![{\displaystyle F\dashv G.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9fa016640d4384f91eb91b39a38e17915a456ed2)

The terminology comes from the [Hilbert space](https://en.wikipedia.org/wiki/Hilbert_space "Hilbert space") idea of [adjoint operators](https://en.wikipedia.org/wiki/Adjoint_operator "Adjoint operator") ![{\displaystyle T}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ec7200acd984a1d3a3d7dc455e262fbe54f7f6e0), ![{\displaystyle U}](https://wikimedia.org/api/rest_v1/media/math/render/svg/458a728f53b9a0274f059cd695e067c430956025) with ![{\displaystyle \langle Ty,x\rangle =\langle y,Ux\rangle }](https://wikimedia.org/api/rest_v1/media/math/render/svg/8c5608ca580862988c4f8dbf5bc368edf5175a03), which is formally similar to the above relation between hom-sets. The analogy to adjoint maps of Hilbert spaces can be made precise in certain contexts.[\[1\]](#cite_note-1)

## Introduction and Motivation

\[[edit](https://en.wikipedia.org/w/index.php?title=Adjoint_functors&action=edit&section=2 "Edit section: Introduction and Motivation")\]

> The slogan is "Adjoint functors arise everywhere".

Common mathematical constructions are very often adjoint functors. Consequently, general theorems about left/right adjoint functors encode the details of many useful and otherwise non-trivial results. Such general theorems include the equivalence of the various definitions of adjoint functors, the uniqueness of a right adjoint for a given left adjoint, the fact that left/right adjoint functors respectively preserve [colimits/limits](https://en.wikipedia.org/wiki/Limit_(category_theory) "Limit (category theory)") (which are also found in every area of mathematics), and the general adjoint functor theorems giving conditions under which a given functor is a left/right adjoint.

### Solutions to optimization problems

\[[edit](https://en.wikipedia.org/w/index.php?title=Adjoint_functors&action=edit&section=3 "Edit section: Solutions to optimization problems")\]

In a sense, an adjoint functor is a way of giving the *most efficient* solution to some problem via a method that is *formulaic*. For example, an elementary problem in [ring theory](https://en.wikipedia.org/wiki/Ring_theory "Ring theory") is how to turn a [rng](https://en.wikipedia.org/wiki/Rng_(algebra) "Rng (algebra)") (which is like a ring that might not have a multiplicative identity) into a [ring](https://en.wikipedia.org/wiki/Ring_(mathematics) "Ring (mathematics)"). The *most efficient* way is to adjoin an element '1' to the rng, adjoin all (and only) the elements that are necessary for satisfying the ring axioms (e.g. *r*+1 for each *r* in the ring), and impose no relations in the newly formed ring that are not forced by axioms. Moreover, this construction is *formulaic* in the sense that it works in essentially the same way for any rng.

This is rather vague, though suggestive, and can be made precise in the language of category theory: a construction is *most efficient* if it satisfies a [universal property](https://en.wikipedia.org/wiki/Universal_property "Universal property"), and is *formulaic* if it defines a [functor](https://en.wikipedia.org/wiki/Functor "Functor"). Universal properties come in two types: initial properties and terminal properties. Since these are [dual](https://en.wikipedia.org/wiki/Dual_(category_theory) "Dual (category theory)") notions, it is only necessary to discuss one of them.

The idea of using an initial property is to set up the problem in terms of some auxiliary category *E*, so that the problem at hand corresponds to finding an [initial object](https://en.wikipedia.org/wiki/Initial_object "Initial object") of *E*. This has an advantage that the *optimization*—the sense that the process finds the *most efficient* solution—means something rigorous and recognisable, rather like the attainment of a [supremum](https://en.wikipedia.org/wiki/Supremum "Supremum"). The category *E* is also formulaic in this construction, since it is always the category of elements of the functor to which one is constructing an adjoint.

Back to our example: take the given rng *R*, and make a category *E* whose *objects* are rng homomorphisms *R* → *S*, with *S* a ring having a multiplicative identity. The *morphisms* in *E* between *R* → *S*1 and *R* → *S*2 are [commutative triangles](https://en.wikipedia.org/wiki/Commutative_diagram "Commutative diagram") of the form (*R* → *S*1, *R* → *S*2, *S*1 → *S*2) where S1 → S2 is a ring map (which preserves the identity). (Note that this is precisely the definition of the [comma category](https://en.wikipedia.org/wiki/Comma_category "Comma category") of *R* over the inclusion of unitary rings into rng.) The existence of a morphism between *R* → *S*1 and *R* → *S*2 implies that *S*1 is at least as efficient a solution as *S*2 to our problem: *S*2 can have more adjoined elements and/or more relations not imposed by axioms than *S*1. Therefore, the assertion that an object *R* → *R\** is initial in *E*, that is, that there is a morphism from it to any other element of *E*, means that the ring *R*\* is a *most efficient* solution to our problem.

The two facts that this method of turning rngs into rings is *most efficient* and *formulaic* can be expressed simultaneously by saying that it defines an *adjoint functor*. More explicitly: Let *F* denote the above process of adjoining an identity to a rng, so *F*(*R*)=*R\**. Let *G* denote the process of “forgetting″ whether a ring *S* has an identity and considering it simply as a rng, so essentially *G*(*S*)=*S*. Then *F* is the *left adjoint functor* of *G*.

Note however that we haven't actually constructed *R\** yet; it is an important and not altogether trivial algebraic fact that such a left adjoint functor *R* → *R\** actually exists.

### Symmetry of optimization problems

\[[edit](https://en.wikipedia.org/w/index.php?title=Adjoint_functors&action=edit&section=4 "Edit section: Symmetry of optimization problems")\]

It is also possible to *start* with the functor *F*, and pose the following (vague) question: is there a problem to which *F* is the most efficient solution?

The notion that *F* is the *most efficient solution* to the problem posed by *G* is, in a certain rigorous sense, equivalent to the notion that *G* poses the *most difficult problem* that *F* solves.

This gives the intuition behind the fact that adjoint functors occur in pairs: if *F* is left adjoint to *G*, then *G* is right adjoint to *F*.

There are various equivalent definitions for adjoint functors:

-   The definitions via universal morphisms are easy to state, and require minimal verifications when constructing an adjoint functor or proving two functors are adjoint. They are also the most analogous to our intuition involving optimizations.
-   The definition via hom-sets makes symmetry the most apparent, and is the reason for using the word *adjoint*.
-   The definition via counit–unit adjunction is convenient for proofs about functors that are known to be adjoint, because they provide formulas that can be directly manipulated.

The equivalency of these definitions is quite useful. Adjoint functors arise everywhere, in all areas of mathematics. Since the structure in any of these definitions gives rise to the structures in the others, switching between them makes implicit use of many details that would otherwise have to be repeated separately in every subject area.

The theory of adjoints has the terms *left* and *right* at its foundation, and there are many components that live in one of two categories *C* and *D* that are under consideration. Therefore it can be helpful to choose letters in alphabetical order according to whether they live in the "lefthand" category *C* or the "righthand" category *D*, and also to write them down in this order whenever possible.

In this article for example, the letters *X*, *F*, *f*, ε will consistently denote things that live in the category *C*, the letters *Y*, *G*, *g*, η will consistently denote things that live in the category *D*, and whenever possible such things will be referred to in order from left to right (a functor *F* : *D* → *C* can be thought of as "living" where its outputs are, in *C*). If the arrows for the left adjoint functor F were drawn they would be pointing to the left; if the arrows for the right adjoint functor G were drawn they would be pointing to the right.

### Definition via universal morphisms

\[[edit](https://en.wikipedia.org/w/index.php?title=Adjoint_functors&action=edit&section=7 "Edit section: Definition via universal morphisms")\]

By definition, a functor ![{\displaystyle F:D\to C}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8721f2760135d2d7ad59755f3e12a63057c18690) is a **left adjoint functor** if for each object ![{\displaystyle X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/68baa052181f707c662844a465bfeeb135e82bab) in ![{\displaystyle C}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4fc55753007cd3c18576f7933f6f089196732029) there exists a [universal morphism](https://en.wikipedia.org/wiki/Universal_morphism "Universal morphism") from ![{\displaystyle F}](https://wikimedia.org/api/rest_v1/media/math/render/svg/545fd099af8541605f7ee55f08225526be88ce57) to ![{\displaystyle X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/68baa052181f707c662844a465bfeeb135e82bab). Spelled out, this means that for each object ![{\displaystyle X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/68baa052181f707c662844a465bfeeb135e82bab) in ![{\displaystyle C}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4fc55753007cd3c18576f7933f6f089196732029) there exists an object ![{\displaystyle G(X)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6286b58ec31d355d6291e63760d5025dab75a99f) in ![{\displaystyle D}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f34a0c600395e5d4345287e21fb26efd386990e6) and a morphism ![{\displaystyle \epsilon _{X}:F(G(X))\to X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/76fb447aa1705cf99815e1b5fa85d3064f2d72a1) such that for every object ![{\displaystyle Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/961d67d6b454b4df2301ac571808a3538b3a6d3f) in ![{\displaystyle D}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f34a0c600395e5d4345287e21fb26efd386990e6) and every morphism ![{\displaystyle f:F(Y)\to X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2b6786a7bca78354ccaeedc955810c0006d77310) there exists a unique morphism ![{\displaystyle g:Y\to G(X)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/86236a121b4c8e5fa2f813634ae3592ded1937c3) with ![{\displaystyle \epsilon _{X}\circ F(g)=f}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2373f7fb2b31f562730a96906ddcb96770deee9f).

The latter equation is expressed by the following [commutative diagram](https://en.wikipedia.org/wiki/Commutative_diagram "Commutative diagram"):

[![Here the counit is a universal morphism.](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Definition_of_the_counit_of_an_adjunction.svg/239px-Definition_of_the_counit_of_an_adjunction.svg.png)](https://en.wikipedia.org/wiki/File:Definition_of_the_counit_of_an_adjunction.svg "Here the counit is a universal morphism.")

Here the counit is a universal morphism.

In this situation, one can show that ![{\displaystyle G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f5f3c8921a3b352de45446a6789b104458c9f90b) can be turned into a functor ![{\displaystyle G:C\to D}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0bb12d089c674d23d680edc6a8e78553b3679f82) in a unique way such that ![{\displaystyle \epsilon _{X}\circ F(G(f))=f\circ \epsilon _{X'}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/426abb709b1704a52bf9e31cf03063a6071d16fe) for all morphisms ![{\displaystyle f:X'\to X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9454ea66877cf385ab67de95634a63d7588f9ed4) in ![{\displaystyle C}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4fc55753007cd3c18576f7933f6f089196732029); ![{\displaystyle F}](https://wikimedia.org/api/rest_v1/media/math/render/svg/545fd099af8541605f7ee55f08225526be88ce57) is then called a **left adjoint** to ![{\displaystyle G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f5f3c8921a3b352de45446a6789b104458c9f90b).

Similarly, we may define right-adjoint functors. A functor ![{\displaystyle G:C\to D}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0bb12d089c674d23d680edc6a8e78553b3679f82) is a **right adjoint functor** if for each object ![{\displaystyle Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/961d67d6b454b4df2301ac571808a3538b3a6d3f) in ![{\displaystyle D}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f34a0c600395e5d4345287e21fb26efd386990e6), there exists a [universal morphism](https://en.wikipedia.org/wiki/Universal_morphism "Universal morphism") from ![{\displaystyle Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/961d67d6b454b4df2301ac571808a3538b3a6d3f) to ![{\displaystyle G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f5f3c8921a3b352de45446a6789b104458c9f90b). Spelled out, this means that for each object ![{\displaystyle Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/961d67d6b454b4df2301ac571808a3538b3a6d3f) in ![{\displaystyle D}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f34a0c600395e5d4345287e21fb26efd386990e6), there exists an object ![{\displaystyle F(Y)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6a83d7ac1ad83b063f816e73ed8c13c8c8297334) in ![{\displaystyle C}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4fc55753007cd3c18576f7933f6f089196732029) and a morphism ![{\displaystyle \eta _{Y}:Y\to G(F(Y))}](https://wikimedia.org/api/rest_v1/media/math/render/svg/15ca1a7b690b4471e034f0d8d5b3a4a92d9a1b89) such that for every object ![{\displaystyle X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/68baa052181f707c662844a465bfeeb135e82bab) in ![{\displaystyle C}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4fc55753007cd3c18576f7933f6f089196732029) and every morphism ![{\displaystyle g:Y\to G(X)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/86236a121b4c8e5fa2f813634ae3592ded1937c3) there exists a unique morphism ![{\displaystyle f:F(Y)\to X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2b6786a7bca78354ccaeedc955810c0006d77310) with ![{\displaystyle G(f)\circ \eta _{Y}=g}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5ea8fc9aef7954a0e39b16fdd08d008a4618ea08).

[![The existence of the unit, a universal morphism, can prove the existence of an adjunction.](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Definition_of_the_unit_of_an_adjunction_1.svg/234px-Definition_of_the_unit_of_an_adjunction_1.svg.png)](https://en.wikipedia.org/wiki/File:Definition_of_the_unit_of_an_adjunction_1.svg "The existence of the unit, a universal morphism, can prove the existence of an adjunction.")

The existence of the unit, a universal morphism, can prove the existence of an adjunction.

Again, this ![{\displaystyle F}](https://wikimedia.org/api/rest_v1/media/math/render/svg/545fd099af8541605f7ee55f08225526be88ce57) can be uniquely turned into a functor ![{\displaystyle F:D\to C}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8721f2760135d2d7ad59755f3e12a63057c18690) such that ![{\displaystyle G(F(g))\circ \eta _{Y}=\eta _{Y'}\circ g}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5d7492d4f99681d5a0651b449517207c1a41e2fa) for ![{\displaystyle g:Y\to Y'}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c083a500bcdcffecf3c6459455012ef49a39a9c0) a morphism in ![{\displaystyle D}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f34a0c600395e5d4345287e21fb26efd386990e6); ![{\displaystyle G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f5f3c8921a3b352de45446a6789b104458c9f90b) is then called a **right adjoint** to ![{\displaystyle F}](https://wikimedia.org/api/rest_v1/media/math/render/svg/545fd099af8541605f7ee55f08225526be88ce57).

It is true, as the terminology implies, that ![{\displaystyle F}](https://wikimedia.org/api/rest_v1/media/math/render/svg/545fd099af8541605f7ee55f08225526be88ce57) is left adjoint to ![{\displaystyle G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f5f3c8921a3b352de45446a6789b104458c9f90b) if and only if ![{\displaystyle G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f5f3c8921a3b352de45446a6789b104458c9f90b) is right adjoint to ![{\displaystyle F}](https://wikimedia.org/api/rest_v1/media/math/render/svg/545fd099af8541605f7ee55f08225526be88ce57).

These definitions via universal morphisms are often useful for establishing that a given functor is left or right adjoint, because they are minimalistic in their requirements. They are also intuitively meaningful in that finding a universal morphism is like solving an optimization problem.

### Definition via Hom-set adjunction

\[[edit](https://en.wikipedia.org/w/index.php?title=Adjoint_functors&action=edit&section=8 "Edit section: Definition via Hom-set adjunction")\]

A **[hom-set](https://en.wikipedia.org/wiki/Hom-set "Hom-set") adjunction** between two categories *C* and *D* consists of two [functors](https://en.wikipedia.org/wiki/Functor "Functor") *F* : *D* → *C* and *G* : *C* → *D* and a [natural isomorphism](https://en.wikipedia.org/wiki/Natural_isomorphism "Natural isomorphism")

![{\displaystyle \Phi :\mathrm {hom} _{C}(F-,-)\to \mathrm {hom} _{D}(-,G-)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/49f6d53e33fe62bdf576164b388a07af3849a3a5).

This specifies a family of bijections

![{\displaystyle \Phi _{Y,X}:\mathrm {hom} _{C}(FY,X)\to \mathrm {hom} _{D}(Y,GX)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/bbe636ff5777ff4f9eef68a883c606f2bd472194)

for all objects *X* in *C* and *Y* in *D*.

In this situation, ***F* is left adjoint to *G*** and ***G* is right adjoint to *F*** .

This definition is a logical compromise in that it is more difficult to satisfy than the universal morphism definitions, and has fewer immediate implications than the counit–unit definition. It is useful because of its obvious symmetry, and as a stepping-stone between the other definitions.

In order to interpret Φ as a *natural isomorphism*, one must recognize hom*C*(*F*–, –) and hom*D*(–, *G*–) as functors. In fact, they are both [bifunctors](https://en.wikipedia.org/wiki/Bifunctor "Bifunctor") from *D*op × *C* to **Set** (the [category of sets](https://en.wikipedia.org/wiki/Category_of_sets "Category of sets")). For details, see the article on [hom functors](https://en.wikipedia.org/wiki/Hom_functor "Hom functor"). Explicitly, the naturality of Φ means that for all [morphisms](https://en.wikipedia.org/wiki/Morphism "Morphism") *f* : *X* → *X′* in *C* and all morphisms *g* : *Y*′ → *Y* in *D* the following diagram [commutes](https://en.wikipedia.org/wiki/Commutative_diagram "Commutative diagram"):

[![Naturality of Φ](https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Natural_phi.svg/400px-Natural_phi.svg.png)](https://en.wikipedia.org/wiki/File:Natural_phi.svg "Naturality of Φ")

Naturality of Φ

The vertical arrows in this diagram are those induced by composition. Formally, Hom(*Fg*, *f*) : HomC(*FY*, *X*) → HomC(*FY′*, *X′*) is given by *h* → *f o h o Fg* for each *h* in HomC(*FY*, *X*). Hom(*g*, *Gf*) is similar.

### Definition via counit–unit adjunction

\[[edit](https://en.wikipedia.org/w/index.php?title=Adjoint_functors&action=edit&section=9 "Edit section: Definition via counit–unit adjunction")\]

A **counit–unit adjunction** between two categories *C* and *D* consists of two [functors](https://en.wikipedia.org/wiki/Functor "Functor") *F* : *D* → *C* and *G* : *C* → *D* and two [natural transformations](https://en.wikipedia.org/wiki/Natural_transformation "Natural transformation")

![{\displaystyle {\begin{aligned}\varepsilon &:FG\to 1_{\mathcal {C}}\\\eta &:1_{\mathcal {D}}\to GF\end{aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/35a4ff94d4298d9af2eb4175c599b2bf39b413bd)

respectively called the **counit** and the **unit** of the adjunction (terminology from [universal algebra](https://en.wikipedia.org/wiki/Universal_algebra "Universal algebra")), such that the compositions

![{\displaystyle F{\xrightarrow {\;F\eta \;}}FGF{\xrightarrow {\;\varepsilon F\,}}F}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c2264610bb327abf31760adc66b80798a276013e)

![{\displaystyle G{\xrightarrow {\;\eta G\;}}GFG{\xrightarrow {\;G\varepsilon \,}}G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/17f8a05a48cde13820edf7515c0e62b640ca5086)

are the identity transformations 1*F* and 1*G* on *F* and *G* respectively.

In this situation we say that ***F* is left adjoint to *G*** and ***G* is right adjoint to *F*** , and may indicate this relationship by writing  ![{\displaystyle (\varepsilon ,\eta ):F\dashv G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/60335de80f83f077054c31e7ae187e819a01ca96) , or simply  ![{\displaystyle F\dashv G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/721042515894e125efb15c7811026d9941bb55f2) .

In equation form, the above conditions on (*ε*,*η*) are the **counit–unit equations**

![{\displaystyle {\begin{aligned}1_{F}&=\varepsilon F\circ F\eta \\1_{G}&=G\varepsilon \circ \eta G\end{aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/889328fd01cb03250dfb7d454333e9b6e6af2171)

which mean that for each *X* in *C* and each *Y* in *D*,

![{\displaystyle {\begin{aligned}1_{FY}&=\varepsilon _{FY}\circ F(\eta _{Y})\\1_{GX}&=G(\varepsilon _{X})\circ \eta _{GX}\end{aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5fd9e133797e94e40e39de8189e4238e5c4fdef1).

Note that ![{\displaystyle 1_{\mathcal {C}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a411e4a82f603d6a462f3d82976270db9547c8d3) denotes the identify functor on the category ![{\displaystyle {\mathcal {C}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e7b3edab7022ca9e2976651bc59c489513ee9019), ![{\displaystyle 1_{F}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/967cfa20df6bb70ebc56a0e1b74f9a0f48b431a7) denotes the identity natural transformation from the functor *F* to itself, and ![{\displaystyle 1_{FY}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/820d1acbe1d45b539fab6e0149bae50ef7192c99) denotes the identity morphism of the object *FY*.

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/String_diagram_adjunction.svg/220px-String_diagram_adjunction.svg.png)](https://en.wikipedia.org/wiki/File:String_diagram_adjunction.svg)

String diagram for adjunction.

These equations are useful in reducing proofs about adjoint functors to algebraic manipulations. They are sometimes called the *triangle identities*, or sometimes the *zig-zag equations* because of the appearance of the corresponding [string diagrams](https://en.wikipedia.org/wiki/String_diagram "String diagram"). A way to remember them is to first write down the nonsensical equation ![{\displaystyle 1=\varepsilon \circ \eta }](https://wikimedia.org/api/rest_v1/media/math/render/svg/da9341e038f0419a44b950dc9895ff444e4b108d) and then fill in either *F* or *G* in one of the two simple ways that make the compositions defined.

Note: The use of the prefix "co" in counit here is not consistent with the terminology of limits and colimits, because a colimit satisfies an *initial* property whereas the counit morphisms will satisfy *terminal* properties, and dually. The term *unit* here is borrowed from the theory of [monads](https://en.wikipedia.org/wiki/Monad_(category_theory) "Monad (category theory)") where it looks like the insertion of the identity 1 into a monoid.

The idea of adjoint functors was introduced by [Daniel Kan](https://en.wikipedia.org/wiki/Daniel_Kan "Daniel Kan") in 1958.[\[2\]](#cite_note-2) Like many of the concepts in category theory, it was suggested by the needs of [homological algebra](https://en.wikipedia.org/wiki/Homological_algebra "Homological algebra"), which was at the time devoted to computations. Those faced with giving tidy, systematic presentations of the subject would have noticed relations such as

hom(*F*(*X*), *Y*) = hom(*X*, *G*(*Y*))

in the category of [abelian groups](https://en.wikipedia.org/wiki/Abelian_group "Abelian group"), where *F* was the functor ![{\displaystyle -\otimes A}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e6a39f2d707847df173d8fea36d301cbf87dce02) (i.e. take the [tensor product](https://en.wikipedia.org/wiki/Tensor_product "Tensor product") with *A*), and *G* was the functor hom(*A*,–) (this is now known as the [tensor-hom adjunction](https://en.wikipedia.org/wiki/Tensor-hom_adjunction "Tensor-hom adjunction")). The use of the *equals* sign is an [abuse of notation](https://en.wikipedia.org/wiki/Abuse_of_notation "Abuse of notation"); those two groups are not really identical but there is a way of identifying them that is *natural*. It can be seen to be natural on the basis, firstly, that these are two alternative descriptions of the [bilinear mappings](https://en.wikipedia.org/wiki/Bilinear_mapping "Bilinear mapping") from *X* × *A* to *Y*. That is, however, something particular to the case of tensor product. In category theory the 'naturality' of the bijection is subsumed in the concept of a [natural isomorphism](https://en.wikipedia.org/wiki/Natural_isomorphism "Natural isomorphism").

The construction of [free groups](https://en.wikipedia.org/wiki/Free_group "Free group") is a common and illuminating example.

Let *F* : **[Set](https://en.wikipedia.org/wiki/Category_of_sets "Category of sets")** → **[Grp](https://en.wikipedia.org/wiki/Category_of_groups "Category of groups")** be the functor assigning to each set *Y* the [free group](https://en.wikipedia.org/wiki/Free_group "Free group") generated by the elements of *Y*, and let *G* : **Grp** → **Set** be the [forgetful functor](https://en.wikipedia.org/wiki/Forgetful_functor "Forgetful functor"), which assigns to each group *X* its underlying set. Then *F* is left adjoint to *G*:

**Initial morphisms.** For each set *Y*, the set *GFY* is just the underlying set of the free group *FY* generated by *Y*. Let  ![{\displaystyle \eta _{Y}:Y\to GFY}](https://wikimedia.org/api/rest_v1/media/math/render/svg/add3fa3d29b06820ec75772f035fe2e3fa2c7b3c)  be the set map given by "inclusion of generators". This is an initial morphism from *Y* to *G*, because any set map from *Y* to the underlying set *GW* of some group *W* will factor through  ![{\displaystyle \eta _{Y}:Y\to GFY}](https://wikimedia.org/api/rest_v1/media/math/render/svg/add3fa3d29b06820ec75772f035fe2e3fa2c7b3c)  via a unique group homomorphism from *FY* to *W*. This is precisely the [universal property of the free group on *Y*](https://en.wikipedia.org/wiki/Free_group#Universal_property "Free group").

**Terminal morphisms.** For each group *X*, the group *FGX* is the free group generated freely by *GX*, the elements of *X*. Let  ![{\displaystyle \varepsilon _{X}:FGX\to X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/aff793eee6b1fbd1dd83db005fbb4f04ab3f6a33)  be the group homomorphism that sends the generators of *FGX* to the elements of *X* they correspond to, which exists by the universal property of free groups. Then each  ![{\displaystyle (GX,\varepsilon _{X})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/201adf97ae50a5e005284fd79be1bef96ab6a125)  is a terminal morphism from *F* to *X*, because any group homomorphism from a free group *FZ* to *X* will factor through  ![{\displaystyle \varepsilon _{X}:FGX\to X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/aff793eee6b1fbd1dd83db005fbb4f04ab3f6a33)  via a unique set map from *Z* to *GX*. This means that (*F*,*G*) is an adjoint pair.

**Hom-set adjunction.** Group homomorphisms from the free group *FY* to a group *X* correspond precisely to maps from the set *Y* to the set *GX*: each homomorphism from *FY* to *X* is fully determined by its action on generators, another restatement of the universal property of free groups. One can verify directly that this correspondence is a natural transformation, which means it is a hom-set adjunction for the pair (*F*,*G*).

**counit–unit adjunction.** One can also verify directly that ε and η are natural. Then, a direct verification that they form a counit–unit adjunction  ![{\displaystyle (\varepsilon ,\eta ):F\dashv G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/60335de80f83f077054c31e7ae187e819a01ca96)  is as follows:

**The first counit–unit equation**  ![{\displaystyle 1_{F}=\varepsilon F\circ F\eta }](https://wikimedia.org/api/rest_v1/media/math/render/svg/05f4dcfb11f25ee09cf2acba431c943dbf3e19e6)  says that for each set *Y* the composition

![{\displaystyle FY{\xrightarrow {\;F(\eta _{Y})\;}}FGFY{\xrightarrow {\;\varepsilon _{FY}\,}}FY}](https://wikimedia.org/api/rest_v1/media/math/render/svg/fd06f26bd89d1ac934778e5911d97e25ad53a833)

should be the identity. The intermediate group *FGFY* is the free group generated freely by the words of the free group *FY*. (Think of these words as placed in parentheses to indicate that they are independent generators.) The arrow  ![{\displaystyle F(\eta _{Y})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/53b14b63d9c3477dbdbcd312a1e958cc727c7156)  is the group homomorphism from *FY* into *FGFY* sending each generator *y* of *FY* to the corresponding word of length one (*y*) as a generator of *FGFY*. The arrow  ![{\displaystyle \varepsilon _{FY}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b69c1ab273032a97f027766ef09cfbda95fdfd91)  is the group homomorphism from *FGFY* to *FY* sending each generator to the word of *FY* it corresponds to (so this map is "dropping parentheses"). The composition of these maps is indeed the identity on *FY*.

**The second counit–unit equation**  ![{\displaystyle 1_{G}=G\varepsilon \circ \eta G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d68fdcdadd147d2bc61118abc24074e1e96e0f01)  says that for each group *X* the composition

 ![{\displaystyle GX{\xrightarrow {\;\eta _{GX}\;}}GFGX{\xrightarrow {\;G(\varepsilon _{X})\,}}GX}](https://wikimedia.org/api/rest_v1/media/math/render/svg/728f6203033eaac6597d37a7468a6db7b6865285) 

should be the identity. The intermediate set *GFGX* is just the underlying set of *FGX*. The arrow  ![{\displaystyle \eta _{GX}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/68418d9574ab74151117db41034e86453f263b8b)  is the "inclusion of generators" set map from the set *GX* to the set *GFGX*. The arrow  ![{\displaystyle G(\varepsilon _{X})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/bba942e537b742242e825ccfe535a736b8291db4)  is the set map from *GFGX* to *GX*, which underlies the group homomorphism sending each generator of *FGX* to the element of *X* it corresponds to ("dropping parentheses"). The composition of these maps is indeed the identity on *GX*.

### Free constructions and forgetful functors

\[[edit](https://en.wikipedia.org/w/index.php?title=Adjoint_functors&action=edit&section=13 "Edit section: Free constructions and forgetful functors")\]

[Free objects](https://en.wikipedia.org/wiki/Free_object "Free object") are all examples of a left adjoint to a [forgetful functor](https://en.wikipedia.org/wiki/Forgetful_functor "Forgetful functor"), which assigns to an algebraic object its underlying set. These algebraic [free functors](https://en.wikipedia.org/wiki/Free_functor "Free functor") have generally the same description as in the detailed description of the free group situation above.

### Diagonal functors and limits

\[[edit](https://en.wikipedia.org/w/index.php?title=Adjoint_functors&action=edit&section=14 "Edit section: Diagonal functors and limits")\]

[Products](https://en.wikipedia.org/wiki/Product_(category_theory) "Product (category theory)"), [fibred products](https://en.wikipedia.org/wiki/Pullback_(category_theory) "Pullback (category theory)"), [equalizers](https://en.wikipedia.org/wiki/Equalizer_(mathematics) "Equalizer (mathematics)"), and [kernels](https://en.wikipedia.org/wiki/Kernel_(algebra) "Kernel (algebra)") are all examples of the categorical notion of a [limit](https://en.wikipedia.org/wiki/Limit_(category_theory) "Limit (category theory)"). Any limit functor is right adjoint to a corresponding diagonal functor (provided the category has the type of limits in question), and the counit of the adjunction provides the defining maps from the limit object (i.e. from the diagonal functor on the limit, in the functor category). Below are some specific examples.

-   **Products** Let Π : **Grp2** → **Grp** be the functor that assigns to each pair (*X*1, *X2*) the product group *X*1×*X*2, and let Δ : **Grp →** **Grp2** be the [diagonal functor](https://en.wikipedia.org/wiki/Diagonal_functor "Diagonal functor") that assigns to every group *X* the pair (*X*, *X*) in the product category **Grp2**. The universal property of the product group shows that Π is right-adjoint to Δ. The counit of this adjunction is the defining pair of projection maps from *X*1×*X*2 to *X*1 and *X*2 which define the limit, and the unit is the *diagonal inclusion* of a group X into *X*×*X* (mapping x to (x,x)).

The [cartesian product](https://en.wikipedia.org/wiki/Cartesian_product "Cartesian product") of [sets](https://en.wikipedia.org/wiki/Set_(mathematics) "Set (mathematics)"), the product of rings, the [product of topological spaces](https://en.wikipedia.org/wiki/Product_topology "Product topology") etc. follow the same pattern; it can also be extended in a straightforward manner to more than just two factors. More generally, any type of limit is right adjoint to a diagonal functor.

-   **Kernels.** Consider the category *D* of homomorphisms of abelian groups. If *f*1 : *A*1 → *B*1 and *f*2 : *A*2 → *B*2 are two objects of *D*, then a morphism from *f*1 to *f*2 is a pair (*g**A*, *g**B*) of morphisms such that *g**B**f*1 = *f*2*g**A*. Let *G* : *D* → **Ab** be the functor which assigns to each homomorphism its [kernel](https://en.wikipedia.org/wiki/Kernel_(algebra) "Kernel (algebra)") and let *F* : **Ab →** *D* be the functor which maps the group *A* to the homomorphism *A* → 0. Then *G* is right adjoint to *F*, which expresses the universal property of kernels. The counit of this adjunction is the defining embedding of a homomorphism's kernel into the homomorphism's domain, and the unit is the morphism identifying a group *A* with the kernel of the homomorphism *A* → 0.

A suitable variation of this example also shows that the kernel functors for vector spaces and for modules are right adjoints. Analogously, one can show that the cokernel functors for abelian groups, vector spaces and modules are left adjoints.

### Colimits and diagonal functors

\[[edit](https://en.wikipedia.org/w/index.php?title=Adjoint_functors&action=edit&section=15 "Edit section: Colimits and diagonal functors")\]

[Coproducts](https://en.wikipedia.org/wiki/Coproduct "Coproduct"), [fibred coproducts](https://en.wikipedia.org/wiki/Pushout_(category_theory) "Pushout (category theory)"), [coequalizers](https://en.wikipedia.org/wiki/Coequalizer "Coequalizer"), and [cokernels](https://en.wikipedia.org/wiki/Cokernel "Cokernel") are all examples of the categorical notion of a [colimit](https://en.wikipedia.org/wiki/Limit_(category_theory) "Limit (category theory)"). Any colimit functor is left adjoint to a corresponding diagonal functor (provided the category has the type of colimits in question), and the unit of the adjunction provides the defining maps into the colimit object. Below are some specific examples.

-   **Coproducts.** If *F* : **Ab****2** **→** **Ab** assigns to every pair (*X*1, *X*2) of abelian groups their [direct sum](https://en.wikipedia.org/wiki/Direct_sum_of_groups "Direct sum of groups"), and if *G* : **Ab** → **Ab****2** is the functor which assigns to every abelian group *Y* the pair (*Y*, *Y*), then *F* is left adjoint to *G*, again a consequence of the universal property of direct sums. The unit of this adjoint pair is the defining pair of inclusion maps from *X*1 and *X*2 into the direct sum, and the counit is the additive map from the direct sum of (*X*,*X*) to back to *X* (sending an element (*a*,*b*) of the direct sum to the element *a*+*b* of *X*).

Analogous examples are given by the [direct sum](https://en.wikipedia.org/wiki/Direct_sum_of_modules "Direct sum of modules") of [vector spaces](https://en.wikipedia.org/wiki/Vector_space "Vector space") and [modules](https://en.wikipedia.org/wiki/Module_(mathematics) "Module (mathematics)"), by the [free product](https://en.wikipedia.org/wiki/Free_product "Free product") of groups and by the disjoint union of sets.

-   **Adjoining an identity to a [rng](https://en.wikipedia.org/wiki/Rng_(algebra) "Rng (algebra)").** This example was discussed in the motivation section above. Given a rng *R*, a multiplicative identity element can be added by taking *R*x**Z** and defining a **Z**\-bilinear product with (r,0)(0,1) = (0,1)(r,0) = (r,0), (r,0)(s,0) = (rs,0), (0,1)(0,1) = (0,1). This constructs a left adjoint to the functor taking a ring to the underlying rng.
-   **Adjoining an identity to a [semigroup](https://en.wikipedia.org/wiki/Semigroup "Semigroup").** Similarly, given a semigroup *S*, we can add an identity element and obtain a [monoid](https://en.wikipedia.org/wiki/Monoid "Monoid") by taking the [disjoint union](https://en.wikipedia.org/wiki/Disjoint_union "Disjoint union") *S* ![{\displaystyle \sqcup }](https://wikimedia.org/api/rest_v1/media/math/render/svg/1596aedf354da694149e44ce2bf53ede54eca8cb) {1} and defining a binary operation on it such that it extends the operation on *S* and 1 is an identity element. This construction gives a functor that is a left adjoint to the functor taking a monoid to the underlying semigroup.
-   **Ring extensions.** Suppose *R* and *S* are rings, and ρ : *R* → *S* is a [ring homomorphism](https://en.wikipedia.org/wiki/Ring_homomorphism "Ring homomorphism"). Then *S* can be seen as a (left) *R*\-module, and the [tensor product](https://en.wikipedia.org/wiki/Tensor_product "Tensor product") with *S* yields a functor *F* : *R*\-**Mod** → *S*\-**Mod**. Then *F* is left adjoint to the forgetful functor *G* : *S*\-**Mod** → *R*\-**Mod**.
-   **[Tensor products](https://en.wikipedia.org/wiki/Tensor-hom_adjunction "Tensor-hom adjunction").** If *R* is a ring and *M* is a right *R*\-module, then the tensor product with *M* yields a functor *F* : *R*\-**Mod** → **Ab**. The functor *G* : **Ab** → *R*\-**Mod**, defined by *G*(*A*) = hom**Z**(*M*,*A*) for every abelian group *A*, is a right adjoint to *F*.
-   **From monoids and groups to rings.** The [integral monoid ring](https://en.wikipedia.org/wiki/Integral_monoid_ring "Integral monoid ring") construction gives a functor from [monoids](https://en.wikipedia.org/wiki/Monoid "Monoid") to rings. This functor is left adjoint to the functor that associates to a given ring its underlying multiplicative monoid. Similarly, the [integral group ring](https://en.wikipedia.org/wiki/Integral_group_ring "Integral group ring") construction yields a functor from [groups](https://en.wikipedia.org/wiki/Group_(mathematics) "Group (mathematics)") to rings, left adjoint to the functor that assigns to a given ring its [group of units](https://en.wikipedia.org/wiki/Group_of_units "Group of units"). One can also start with a [field](https://en.wikipedia.org/wiki/Field_(mathematics) "Field (mathematics)") *K* and consider the category of *K*\-[algebras](https://en.wikipedia.org/wiki/Associative_algebra "Associative algebra") instead of the category of rings, to get the monoid and group rings over *K*.
-   **Field of fractions.** Consider the category **Dom**m of integral domains with injective morphisms. The forgetful functor **Field** → **Dom**m from fields has a left adjoint—it assigns to every integral domain its [field of fractions](https://en.wikipedia.org/wiki/Field_of_fractions "Field of fractions").
-   **Polynomial rings**. Let **Ring**\* be the category of pointed commutative rings with unity (pairs (A,a) where A is a ring, a ∈ A and morphisms preserve the distinguished elements). The forgetful functor G:**Ring**\* → **Ring** has a left adjoint – it assigns to every ring R the pair (R\[x\],x) where R\[x\] is the [polynomial ring](https://en.wikipedia.org/wiki/Polynomial_ring "Polynomial ring") with coefficients from R.
-   **Abelianization**. Consider the inclusion functor *G* : **Ab** → **Grp** from the [category of abelian groups](https://en.wikipedia.org/wiki/Category_of_abelian_groups "Category of abelian groups") to [category of groups](https://en.wikipedia.org/wiki/Category_of_groups "Category of groups"). It has a left adjoint called [abelianization](https://en.wikipedia.org/wiki/Abelianization "Abelianization") which assigns to every group *G* the quotient group *G*ab\=*G*/\[*G*,*G*\].
-   **The Grothendieck group**. In [K-theory](https://en.wikipedia.org/wiki/K-theory "K-theory"), the point of departure is to observe that the category of [vector bundles](https://en.wikipedia.org/wiki/Vector_bundle "Vector bundle") on a [topological space](https://en.wikipedia.org/wiki/Topological_space "Topological space") has a commutative monoid structure under [direct sum](https://en.wikipedia.org/wiki/Direct_sum_of_modules "Direct sum of modules"). One may make an [abelian group](https://en.wikipedia.org/wiki/Abelian_group "Abelian group") out of this monoid, the [Grothendieck group](https://en.wikipedia.org/wiki/Grothendieck_group "Grothendieck group"), by formally adding an additive inverse for each bundle (or equivalence class). Alternatively one can observe that the functor that for each group takes the underlying monoid (ignoring inverses) has a left adjoint. This is a once-for-all construction, in line with the third section discussion above. That is, one can imitate the construction of [negative numbers](https://en.wikipedia.org/wiki/Negative_number "Negative number"); but there is the other option of an [existence theorem](https://en.wikipedia.org/wiki/Existence_theorem "Existence theorem"). For the case of finitary algebraic structures, the existence by itself can be referred to [universal algebra](https://en.wikipedia.org/wiki/Universal_algebra "Universal algebra"), or [model theory](https://en.wikipedia.org/wiki/Model_theory "Model theory"); naturally there is also a proof adapted to category theory, too.
-   **Frobenius reciprocity** in the [representation theory of groups](https://en.wikipedia.org/wiki/Group_representation "Group representation"): see [induced representation](https://en.wikipedia.org/wiki/Induced_representation "Induced representation"). This example foreshadowed the general theory by about half a century.

-   **A functor with a left and a right adjoint.** Let *G* be the functor from [topological spaces](https://en.wikipedia.org/wiki/Topological_space "Topological space") to [sets](https://en.wikipedia.org/wiki/Set_(mathematics) "Set (mathematics)") that associates to every topological space its underlying set (forgetting the topology, that is). *G* has a left adjoint *F*, creating the [discrete space](https://en.wikipedia.org/wiki/Discrete_space "Discrete space") on a set *Y*, and a right adjoint *H* creating the [trivial topology](https://en.wikipedia.org/wiki/Trivial_topology "Trivial topology") on *Y*.
-   **Suspensions and loop spaces.** Given [topological spaces](https://en.wikipedia.org/wiki/Topological_spaces "Topological spaces") *X* and *Y*, the space \[*SX*, *Y*\] of [homotopy classes](https://en.wikipedia.org/wiki/Homotopy_classes "Homotopy classes") of maps from the [suspension](https://en.wikipedia.org/wiki/Suspension_(topology) "Suspension (topology)") *SX* of *X* to *Y* is naturally isomorphic to the space \[*X*, Ω*Y*\] of homotopy classes of maps from *X* to the [loop space](https://en.wikipedia.org/wiki/Loop_space "Loop space") Ω*Y* of *Y*. The suspension functor is therefore left adjoint to the loop space functor in the [homotopy category](https://en.wikipedia.org/wiki/Homotopy_category "Homotopy category"), an important fact in [homotopy theory](https://en.wikipedia.org/wiki/Homotopy_theory "Homotopy theory").
-   **Stone–Čech compactification.** Let **KHaus** be the category of [compact](https://en.wikipedia.org/wiki/Compact_space "Compact space") [Hausdorff spaces](https://en.wikipedia.org/wiki/Hausdorff_space "Hausdorff space") and *G* : **KHaus** → **Top** be the inclusion functor to the category of [topological spaces](https://en.wikipedia.org/wiki/Topological_spaces "Topological spaces"). Then *G* has a left adjoint *F* : **Top** → **KHaus**, the [Stone–Čech compactification](https://en.wikipedia.org/wiki/Stone%E2%80%93%C4%8Cech_compactification "Stone–Čech compactification"). The unit of this adjoint pair yields a [continuous](https://en.wikipedia.org/wiki/Continuous_function_(topology) "Continuous function (topology)") map from every topological space *X* into its Stone–Čech compactification.
-   **Direct and inverse images of sheaves.** Every [continuous map](https://en.wikipedia.org/wiki/Continuous_map "Continuous map") *f* : *X* → *Y* between [topological spaces](https://en.wikipedia.org/wiki/Topological_space "Topological space") induces a functor *f* ∗ from the category of [sheaves](https://en.wikipedia.org/wiki/Sheaf_(mathematics) "Sheaf (mathematics)") (of sets, or abelian groups, or rings...) on *X* to the corresponding category of sheaves on *Y*, the *[direct image functor](https://en.wikipedia.org/wiki/Direct_image_functor "Direct image functor")*. It also induces a functor *f* −1 from the category of sheaves of abelian groups on *Y* to the category of sheaves of abelian groups on *X*, the *[inverse image functor](https://en.wikipedia.org/wiki/Inverse_image_functor "Inverse image functor")*. *f* −1 is left adjoint to *f* ∗. Here a more subtle point is that the left adjoint for [coherent sheaves](https://en.wikipedia.org/wiki/Coherent_sheaf "Coherent sheaf") will differ from that for sheaves (of sets).
-   **Soberification.** The article on [Stone duality](https://en.wikipedia.org/wiki/Stone_duality "Stone duality") describes an adjunction between the category of topological spaces and the category of [sober spaces](https://en.wikipedia.org/wiki/Sober_space "Sober space") that is known as soberification. Notably, the article also contains a detailed description of another adjunction that prepares the way for the famous [duality](https://en.wikipedia.org/wiki/Duality_(category_theory) "Duality (category theory)") of sober spaces and spatial locales, exploited in [pointless topology](https://en.wikipedia.org/wiki/Pointless_topology "Pointless topology").

Every [partially ordered set](https://en.wikipedia.org/wiki/Partially_ordered_set "Partially ordered set") can be viewed as a category (where the elements of the poset become the category's objects and we have a single morphism from *x* to *y* if and only if *x* ≤ *y*). A pair of adjoint functors between two partially ordered sets is called a [Galois connection](https://en.wikipedia.org/wiki/Galois_connection "Galois connection") (or, if it is contravariant, an *antitone* Galois connection). See that article for a number of examples: the case of [Galois theory](https://en.wikipedia.org/wiki/Galois_theory "Galois theory") of course is a leading one. Any Galois connection gives rise to [closure operators](https://en.wikipedia.org/wiki/Closure_operator "Closure operator") and to inverse order-preserving bijections between the corresponding closed elements.

As is the case for Galois groups, the real interest lies often in refining a correspondence to a [duality](https://en.wikipedia.org/wiki/Duality_(mathematics) "Duality (mathematics)") (i.e. *antitone* order isomorphism). A treatment of Galois theory along these lines by [Kaplansky](https://en.wikipedia.org/wiki/Irving_Kaplansky "Irving Kaplansky") was influential in the recognition of the general structure here.

The partial order case collapses the adjunction definitions quite noticeably, but can provide several themes:

-   adjunctions may not be dualities or isomorphisms, but are candidates for upgrading to that status
-   closure operators may indicate the presence of adjunctions, as corresponding [monads](https://en.wikipedia.org/wiki/Monad_(category_theory) "Monad (category theory)") (cf. the [Kuratowski closure axioms](https://en.wikipedia.org/wiki/Kuratowski_closure_axioms "Kuratowski closure axioms"))
-   a very general comment of [William Lawvere](https://en.wikipedia.org/wiki/William_Lawvere "William Lawvere")[\[3\]](#cite_note-3) is that *syntax and semantics* are adjoint: take *C* to be the set of all logical theories (axiomatizations), and *D* the power set of the set of all mathematical structures. For a theory *T* in *C*, let *G*(*T*) be the set of all structures that satisfy the axioms *T*; for a set of mathematical structures *S*, let *F*(*S*) be the minimal axiomatization of *S*. We can then say that *S* is a subset of *G*(*T*) if and only if *F*(*S*) logically implies *T*: the "semantics functor" *G* is right adjoint to the "syntax functor" *F*.
-   [division](https://en.wikipedia.org/wiki/Division_(mathematics) "Division (mathematics)") is (in general) the attempt to *invert* multiplication, but in situations where this is not possible, we often attempt to construct an *adjoint* instead: the [ideal quotient](https://en.wikipedia.org/wiki/Ideal_quotient "Ideal quotient") is adjoint to the multiplication by [ring ideals](https://en.wikipedia.org/wiki/Ring_ideal "Ring ideal"), and the [implication](https://en.wikipedia.org/wiki/Material_conditional "Material conditional") in [propositional logic](https://en.wikipedia.org/wiki/Propositional_calculus "Propositional calculus") is adjoint to [logical conjunction](https://en.wikipedia.org/wiki/Logical_conjunction "Logical conjunction").

-   **Equivalences.** If *F* : *D* → *C* is an [equivalence of categories](https://en.wikipedia.org/wiki/Equivalence_of_categories "Equivalence of categories"), then we have an inverse equivalence *G* : *C* → *D*, and the two functors *F* and *G* form an adjoint pair. The unit and counit are natural isomorphisms in this case.
-   **A series of adjunctions.** The functor π0 which assigns to a category its set of connected components is left-adjoint to the functor *D* which assigns to a set the discrete category on that set. Moreover, *D* is left-adjoint to the object functor *U* which assigns to each category its set of objects, and finally *U* is left-adjoint to *A* which assigns to each set the indiscrete category[\[4\]](#cite_note-4) on that set.
-   **Exponential object**. In a [cartesian closed category](https://en.wikipedia.org/wiki/Cartesian_closed_category "Cartesian closed category") the endofunctor *C* → *C* given by –×*A* has a right adjoint –*A*. This pair is often referred to as [currying](https://en.wikipedia.org/wiki/Currying "Currying") and uncurrying; in many special cases, they are also continuous and form a homeomorphism.

The role of [quantifiers](https://en.wikipedia.org/wiki/Quantifier_(logic) "Quantifier (logic)") in predicate logics is in forming propositions and also in expressing sophisticated predicates by closing formulas with possibly more variables. For example, consider a predicate ![{\displaystyle \psi _{f}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c4e82b01997b1879d1a94c618c886471271f3de3) with two open variables of sort ![{\displaystyle X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/68baa052181f707c662844a465bfeeb135e82bab) and ![{\displaystyle Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/961d67d6b454b4df2301ac571808a3538b3a6d3f). Using a quantifier to close ![{\displaystyle X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/68baa052181f707c662844a465bfeeb135e82bab), we can form the set

![{\displaystyle \{y\in Y\mid \exists x.\,\psi _{f}(x,y)\land \phi _{S}(x)\}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/08da7823ac5fe87c1a078bfacb736c3a81412cd0)

of all elements ![{\displaystyle y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b8a6208ec717213d4317e666f1ae872e00620a0d) of ![{\displaystyle Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/961d67d6b454b4df2301ac571808a3538b3a6d3f) for which there is an ![{\displaystyle x}](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4) to which it is ![{\displaystyle \psi _{f}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c4e82b01997b1879d1a94c618c886471271f3de3)\-related, and which itself is characterized by the property ![{\displaystyle \phi _{S}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/51f66224fdb3930fba0a321d8409e0547cbf4829). Set theoretic operations like the intersection ![{\displaystyle \cap }](https://wikimedia.org/api/rest_v1/media/math/render/svg/9d4e886e6f5a28a33e073fb108440c152ecfe2d3) of two sets directly corresponds to the conjunction ![{\displaystyle \land }](https://wikimedia.org/api/rest_v1/media/math/render/svg/d6823e5a222eb3ca49672818ac3d13ec607052c4) of predicates. In [categorical logic](https://en.wikipedia.org/wiki/Categorical_logic "Categorical logic"), a subfield of [topos theory](https://en.wikipedia.org/wiki/Topos_theory "Topos theory"), quantifiers are identified with adjoints to the pullback functor. Such a realization can be seen in analogy to the discussion of propositional logic using set theory but the general definition make for a richer range of logics.

So consider an object ![{\displaystyle Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/961d67d6b454b4df2301ac571808a3538b3a6d3f) in a category with pullbacks. Any morphism ![{\displaystyle f:X\to Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/abd1e080abef4bbdab67b43819c6431e7561361c) induces a functor

![{\displaystyle f^{*}:{\text{Sub}}(Y)\longrightarrow {\text{Sub}}(X)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/62f73798ff24bb04ac26b2377fa0355e92b75646)

on the category that is the preorder of [subobjects](https://en.wikipedia.org/wiki/Subobject "Subobject"). It maps subobjects ![{\displaystyle T}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ec7200acd984a1d3a3d7dc455e262fbe54f7f6e0) of ![{\displaystyle Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/961d67d6b454b4df2301ac571808a3538b3a6d3f) (technically: monomorphism classes of ![{\displaystyle T\to Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4acfa7511f1a46baab3346d050df50b82f2ef141)) to the pullback ![{\displaystyle X\times _{Y}T}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4c27e4084d210b99cda859aa4b8fa3c005db74f0). If this functor has a left- or right adjoint, they are called ![{\displaystyle \exists _{f}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2a82acacd0c36c028cd8fa527c634090ea496908) and ![{\displaystyle \forall _{f}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5ca2bf0b3bccb6b57c37922ef7d50ce685e8531c), respectively.[\[5\]](#cite_note-5) They both map from ![{\displaystyle {\text{Sub}}(X)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f09c42207f9efc8a5f47e6d1413dc51b07160c69) back to ![{\displaystyle {\text{Sub}}(Y)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/bfc1461721a9e345decd9b36bf9aec14d4a5ec47). Very roughly, given a domain ![{\displaystyle S\subset X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/616c8a284e5623c9ca7184dddef9b84da4cd251b) to quantify a relation expressed via ![{\displaystyle f}](https://wikimedia.org/api/rest_v1/media/math/render/svg/132e57acb643253e7810ee9702d9581f159a1c61) over, the functor/quantifier closes ![{\displaystyle X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/68baa052181f707c662844a465bfeeb135e82bab) in ![{\displaystyle X\times _{Y}T}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4c27e4084d210b99cda859aa4b8fa3c005db74f0) and returns the thereby specified subset of ![{\displaystyle Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/961d67d6b454b4df2301ac571808a3538b3a6d3f).

**Example**: In ![{\displaystyle \operatorname {Set} }](https://wikimedia.org/api/rest_v1/media/math/render/svg/e16771fd1a4471c4bc25c7f40de9cca25fffbb38), the category of sets and functions, the canonical subobjects are the subset (or rather their canonical injections). The pullback ![{\displaystyle f^{*}T=X\times _{Y}T}](https://wikimedia.org/api/rest_v1/media/math/render/svg/eaf9e68c164710f651088b2bc96c8aff970e1e63) of an injection of a subset ![{\displaystyle T}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ec7200acd984a1d3a3d7dc455e262fbe54f7f6e0) into ![{\displaystyle Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/961d67d6b454b4df2301ac571808a3538b3a6d3f) along ![{\displaystyle f}](https://wikimedia.org/api/rest_v1/media/math/render/svg/132e57acb643253e7810ee9702d9581f159a1c61) is characterized as the largest set which knows all about ![{\displaystyle f}](https://wikimedia.org/api/rest_v1/media/math/render/svg/132e57acb643253e7810ee9702d9581f159a1c61) and the injection of ![{\displaystyle T}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ec7200acd984a1d3a3d7dc455e262fbe54f7f6e0) into ![{\displaystyle Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/961d67d6b454b4df2301ac571808a3538b3a6d3f). It therefore turns out to be (in bijection with) the inverse image ![{\displaystyle f^{-1}[T]\subseteq X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4a55cb02881c04c713a24cbe82ece550243ab558).

For ![{\displaystyle S\subseteq X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/44aba72977e43f863dd873b095d1dc0bd3f17608), let us figure out the left adjoint, which is defined via

![{\displaystyle {\operatorname {Hom} }(\exists _{f}S,T)\cong {\operatorname {Hom} }(S,f^{*}T),}](https://wikimedia.org/api/rest_v1/media/math/render/svg/586a4eca145a5db0c1afc8c85ce7d5681456829f)

which here just means

![{\displaystyle \exists _{f}S\subseteq T\leftrightarrow S\subseteq f^{-1}[T]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8c821337e6e35974fb9c9d1977c1a3b5da169aab).

Consider ![{\displaystyle f[S]\subseteq T}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6b5dbaa58a61b4955053e8d30ee59bfe257e6c4c). We see ![{\displaystyle S\subseteq f^{-1}[f[S]]\subseteq f^{-1}[T]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9c2845f7f5ca6c49df476c5de6e8c4c4385f1539). Conversely, If for an ![{\displaystyle x\in S}](https://wikimedia.org/api/rest_v1/media/math/render/svg/51186ba8afb2067573a9082d55dd383df1ea9214) we also have ![{\displaystyle x\in f^{-1}[T]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/43e43732bf6ed7b2b03201f6bbb1eea85f573f74), then clearly ![{\displaystyle f(x)\in T}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d242060f2d15829103fd237efb890d7a3a1ed3aa). So ![{\displaystyle S\subseteq f^{-1}[T]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/bad773de89f2d30a93a8442ac7c86eb44e8980bd) implies ![{\displaystyle f[S]\subseteq T}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6b5dbaa58a61b4955053e8d30ee59bfe257e6c4c). We conclude that left adjoint to the inverse image functor ![{\displaystyle f^{*}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/190a73fde235865b8d2a783334f90194331c7f19) is given by the direct image. Here is a characterization of this result, which matches more the logical interpretation: The image of ![{\displaystyle S}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4611d85173cd3b508e67077d4a1252c9c05abca2) under ![{\displaystyle \exists _{f}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2a82acacd0c36c028cd8fa527c634090ea496908) is the full set of ![{\displaystyle y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b8a6208ec717213d4317e666f1ae872e00620a0d)'s, such that ![{\displaystyle f^{-1}[\{y\}]\cap S}](https://wikimedia.org/api/rest_v1/media/math/render/svg/872d2d997b54463e913e7ea72920cfe094e89342) is non-empty. This works because it neglects exactly those ![{\displaystyle y\in Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/cee1c0ec36a82f33f5e3d7434d5667881b4ec323) which are in the complement of ![{\displaystyle f[S]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/dc136e58f23572a4001b784eea645e59b735ce49). So

![{\displaystyle \exists _{f}S=\{y\in Y\mid \exists (x\in f^{-1}[\{y\}]).\,x\in S\;\}=f[S].}](https://wikimedia.org/api/rest_v1/media/math/render/svg/24265e6a1e4e9b58e13a76ba7662185d2527e460)

Put this in analogy to our motivation ![{\displaystyle \{y\in Y\mid \exists x.\,\psi _{f}(x,y)\land \phi _{S}(x)\}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/08da7823ac5fe87c1a078bfacb736c3a81412cd0).

The right adjoint to the inverse image functor is given (without doing the computation here) by

![{\displaystyle \forall _{f}S=\{y\in Y\mid \forall (x\in f^{-1}[\{y\}]).\,x\in S\;\}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a92d205846301c35cf45cd5cf9e17c4fd5937bd3)

The subset ![{\displaystyle \forall _{f}S}](https://wikimedia.org/api/rest_v1/media/math/render/svg/fce085fd559b13f4af0325428851a766a25dc735) of ![{\displaystyle Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/961d67d6b454b4df2301ac571808a3538b3a6d3f) is characterized as the full set of ![{\displaystyle y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b8a6208ec717213d4317e666f1ae872e00620a0d)'s with the property that the inverse image of ![{\displaystyle \{y\}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/144dbb8cb5d9e202a8d1ead595f39c167238858c) with respect to ![{\displaystyle f}](https://wikimedia.org/api/rest_v1/media/math/render/svg/132e57acb643253e7810ee9702d9581f159a1c61) is fully contained within ![{\displaystyle S}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4611d85173cd3b508e67077d4a1252c9c05abca2). Note how the predicate determining the set is the same as above, except that ![{\displaystyle \exists }](https://wikimedia.org/api/rest_v1/media/math/render/svg/77ed842b6b90b2fdd825320cf8e5265fa937b583) is replaced by ![{\displaystyle \forall }](https://wikimedia.org/api/rest_v1/media/math/render/svg/bfc1a1a9c4c0f8d5df989c98aa2773ed657c5937).

*See also [powerset](https://en.wikipedia.org/wiki/Powerset "Powerset").*

The twin fact in probability can be understood as an adjunction: that expectation commutes with affine transform, and that the expectation is in some sense the best *solution* to the problem of finding a real-valued approximation to a distribution on the real numbers.

Define a category based on ![{\displaystyle \mathbb {R} }](https://wikimedia.org/api/rest_v1/media/math/render/svg/786849c765da7a84dbc3cce43e96aad58a5868dc), with objects being the real numbers, and the morphisms being "affine functions evaluated at a point". That is, for any affine function ![{\displaystyle f(x)=ax+b}](https://wikimedia.org/api/rest_v1/media/math/render/svg/75c655df4be41082c4bba924beab2c1dc27d019c) and any real number ![{\displaystyle r}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0d1ecb613aa2984f0576f70f86650b7c2a132538), define a morphism ![{\displaystyle (r,f):r\to f(r)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/02acf13684872c0d7f560ff6bccf59d6f5e5d66e).

Define a category based on ![{\displaystyle M(\mathbb {R} )}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4eaf439ced177f6d051564239cfc4a0842b628dd), the set of probability distribution on ![{\displaystyle \mathbb {R} }](https://wikimedia.org/api/rest_v1/media/math/render/svg/786849c765da7a84dbc3cce43e96aad58a5868dc) with finite expectation. Define morphisms on ![{\displaystyle M(\mathbb {R} )}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4eaf439ced177f6d051564239cfc4a0842b628dd) as "affine functions evaluated at a distribution". That is, for any affine function ![{\displaystyle f(x)=ax+b}](https://wikimedia.org/api/rest_v1/media/math/render/svg/75c655df4be41082c4bba924beab2c1dc27d019c) and any ![{\displaystyle \mu \in M(\mathbb {R} )}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0deb1e500626a9ac6548caf8d93f705f9b380aea), define a morphism ![{\displaystyle (\mu ,f):\mu \to \mu \circ f^{-1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4ce733d52ded775783918993c6d9760d793a4261).

Then, the [Dirac delta measure](https://en.wikipedia.org/wiki/Dirac_delta_measure "Dirac delta measure") defines a functor: ![{\displaystyle \delta :x\mapsto \delta _{x}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c609bd03ba0b2a889b901f04eb3c51e566a78b7a), and the expectation defines another functor ![{\displaystyle \mathbb {E} :\mu \mapsto \mathbb {E} [\mu ]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/1dbb67a1098a8750cec80a69e8213449b0505576), and they are adjoint: ![{\displaystyle \mathbb {E} \dashv \delta }](https://wikimedia.org/api/rest_v1/media/math/render/svg/ed6e8d802a50be635425d2cf1a6c8f2bbe6b8bef). (Somewhat disconcertingly, ![{\displaystyle \mathbb {E} }](https://wikimedia.org/api/rest_v1/media/math/render/svg/ad9faf1fd4a61d36d7f8a2f3204f3805a43c0d4a) is the left adjoint, even though ![{\displaystyle \mathbb {E} }](https://wikimedia.org/api/rest_v1/media/math/render/svg/ad9faf1fd4a61d36d7f8a2f3204f3805a43c0d4a) is "forgetful" and ![{\displaystyle \delta }](https://wikimedia.org/api/rest_v1/media/math/render/svg/c5321cfa797202b3e1f8620663ff43c4660ea03a) is "free".)

## Adjunctions in full

\[[edit](https://en.wikipedia.org/w/index.php?title=Adjoint_functors&action=edit&section=23 "Edit section: Adjunctions in full")\]

There are hence numerous functors and natural transformations associated with every adjunction, and only a small portion is sufficient to determine the rest.

An *adjunction* between categories *C* and *D* consists of

-   A [functor](https://en.wikipedia.org/wiki/Functor "Functor") *F* : *D* → *C* called the **left adjoint**
-   A functor *G* : *C* → *D* called the **right adjoint**
-   A [natural isomorphism](https://en.wikipedia.org/wiki/Natural_isomorphism "Natural isomorphism") Φ : hom*C*(*F*–,–) → hom*D*(–,*G*–)
-   A [natural transformation](https://en.wikipedia.org/wiki/Natural_transformation "Natural transformation") ε : *FG* → 1*C* called the **counit**
-   A natural transformation η : 1*D* → *GF* called the **unit**

An equivalent formulation, where *X* denotes any object of *C* and *Y* denotes any object of *D*, is as follows:

For every *C*\-morphism *f* : *FY* → *X*, there is a unique *D*\-morphism Φ*Y*, *X*(*f*) = *g* : *Y* → *GX* such that the diagrams below commute, and for every *D*\-morphism *g* : *Y* → *GX*, there is a unique *C*\-morphism Φ−1*Y*, *X*(*g*) = *f* : *FY* → *X* in *C* such that the diagrams below commute:

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Adjoint_functors_sym.svg/350px-Adjoint_functors_sym.svg.png)](https://en.wikipedia.org/wiki/File:Adjoint_functors_sym.svg)

From this assertion, one can recover that:

-   The transformations ε, η, and Φ are related by the equations

![{\displaystyle {\begin{aligned}f=\Phi _{Y,X}^{-1}(g)&=\varepsilon _{X}\circ F(g)&\in &\,\,\mathrm {hom} _{C}(F(Y),X)\\g=\Phi _{Y,X}(f)&=G(f)\circ \eta _{Y}&\in &\,\,\mathrm {hom} _{D}(Y,G(X))\\\Phi _{GX,X}^{-1}(1_{GX})&=\varepsilon _{X}&\in &\,\,\mathrm {hom} _{C}(FG(X),X)\\\Phi _{Y,FY}(1_{FY})&=\eta _{Y}&\in &\,\,\mathrm {hom} _{D}(Y,GF(Y))\\\end{aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a58bbeaa9c7c08e1446fe2c31c55c1669b3c4c32)

-   The transformations ε, η satisfy the counit–unit equations

![{\displaystyle {\begin{aligned}1_{FY}&=\varepsilon _{FY}\circ F(\eta _{Y})\\1_{GX}&=G(\varepsilon _{X})\circ \eta _{GX}\end{aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5fd9e133797e94e40e39de8189e4238e5c4fdef1)

-   Each pair (*GX*, ε*X*) is a [terminal morphism](https://en.wikipedia.org/wiki/Universal_morphism "Universal morphism") from *F* to *X* in *C*
-   Each pair (*FY*, η*Y*) is an [initial morphism](https://en.wikipedia.org/wiki/Universal_morphism "Universal morphism") from *Y* to *G* in *D*

In particular, the equations above allow one to define Φ, ε, and η in terms of any one of the three. However, the adjoint functors *F* and *G* alone are in general not sufficient to determine the adjunction. The equivalence of these situations is demonstrated below.

### Universal morphisms induce hom-set adjunction

\[[edit](https://en.wikipedia.org/w/index.php?title=Adjoint_functors&action=edit&section=24 "Edit section: Universal morphisms induce hom-set adjunction")\]

Given a right adjoint functor *G* : *C* → *D*; in the sense of initial morphisms, one may construct the induced hom-set adjunction by doing the following steps.

-   Construct a functor *F* : *D* → *C* and a natural transformation η.
    -   For each object *Y* in *D*, choose an initial morphism (*F*(*Y*), η*Y*) from *Y* to *G*, so that η*Y* : *Y* → *G*(*F*(*Y*)). We have the map of *F* on objects and the family of morphisms η.
    -   For each *f* : *Y*0 → *Y*1, as (*F*(*Y*0), η*Y*0) is an initial morphism, then factorize η*Y*1 o *f* with η*Y*0 and get *F*(*f*) : *F*(*Y*0) → *F*(*Y*1). This is the map of *F* on morphisms.
    -   The commuting diagram of that factorization implies the commuting diagram of natural transformations, so η : 1*D* → *G* o *F* is a [natural transformation](https://en.wikipedia.org/wiki/Natural_transformation "Natural transformation").
    -   Uniqueness of that factorization and that *G* is a functor implies that the map of *F* on morphisms preserves compositions and identities.
-   Construct a natural isomorphism Φ : hom*C*(*F*\-,-) → hom*D*(-,*G*\-).
    -   For each object *X* in *C*, each object *Y* in *D*, as (*F*(*Y*), η*Y*) is an initial morphism, then Φ*Y*, *X* is a bijection, where Φ*Y*, *X*(*f* : *F*(*Y*) → *X*) = *G*(*f*) o η*Y*.
    -   η is a natural transformation, *G* is a functor, then for any objects *X*0, *X*1 in *C*, any objects *Y*0, *Y*1 in *D*, any *x* : *X*0 → *X*1, any *y* : *Y*1 → *Y*0, we have Φ*Y*1, *X*1(*x* o *f* o *F*(*y*)) = G(x) o *G*(*f*) o *G*(*F*(*y*)) o η*Y*1 = *G*(*x*) o *G*(*f*) o η*Y*0 o *y* = *G*(*x*) o Φ*Y*0, *X*0(*f*) o *y*, and then Φ is natural in both arguments.

A similar argument allows one to construct a hom-set adjunction from the terminal morphisms to a left adjoint functor. (The construction that starts with a right adjoint is slightly more common, since the right adjoint in many adjoint pairs is a trivially defined inclusion or forgetful functor.)

### counit–unit adjunction induces hom-set adjunction

\[[edit](https://en.wikipedia.org/w/index.php?title=Adjoint_functors&action=edit&section=25 "Edit section: counit–unit adjunction induces hom-set adjunction")\]

Given functors *F* : *D* → *C*, *G* : *C* → *D*, and a counit–unit adjunction (ε, η) : *F* ![{\displaystyle \dashv }](https://wikimedia.org/api/rest_v1/media/math/render/svg/a2650629b2a797b6e0457f2133f725e78b882b56) *G*, we can construct a hom-set adjunction by finding the natural transformation Φ : hom*C*(*F*\-,-) → hom*D*(-,*G*\-) in the following steps:

-   For each *f* : *FY* → *X* and each *g* : *Y* → *GX*, define

![{\displaystyle {\begin{aligned}\Phi _{Y,X}(f)=G(f)\circ \eta _{Y}\\\Psi _{Y,X}(g)=\varepsilon _{X}\circ F(g)\end{aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f8171e8c5ee22419b48efeffd6fa2ffe173e60fd)

The transformations Φ and Ψ are natural because η and ε are natural.

-   Using, in order, that *F* is a functor, that ε is natural, and the counit–unit equation 1*FY* = ε*FY* o *F*(η*Y*), we obtain

![{\displaystyle {\begin{aligned}\Psi \Phi f&=\varepsilon _{X}\circ FG(f)\circ F(\eta _{Y})\\&=f\circ \varepsilon _{FY}\circ F(\eta _{Y})\\&=f\circ 1_{FY}=f\end{aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8eb7b2baeebfdcd6352a8b95f32e6c9b10373a07)

hence ΨΦ is the identity transformation.

-   Dually, using that *G* is a functor, that η is natural, and the counit–unit equation 1*GX* = *G*(ε*X*) o η*GX*, we obtain

![{\displaystyle {\begin{aligned}\Phi \Psi g&=G(\varepsilon _{X})\circ GF(g)\circ \eta _{Y}\\&=G(\varepsilon _{X})\circ \eta _{GX}\circ g\\&=1_{GX}\circ g=g\end{aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e3797fb39188a5dc593831697596927c951f1e89)

hence ΦΨ is the identity transformation. Thus Φ is a natural isomorphism with inverse Φ−1 = Ψ.

### Hom-set adjunction induces all of the above

\[[edit](https://en.wikipedia.org/w/index.php?title=Adjoint_functors&action=edit&section=26 "Edit section: Hom-set adjunction induces all of the above")\]

Given functors *F* : *D* → *C*, *G* : *C* → *D*, and a hom-set adjunction Φ : hom*C*(*F*\-,-) → hom*D*(-,*G*\-), one can construct a counit–unit adjunction

![{\displaystyle (\varepsilon ,\eta ):F\dashv G}](https://wikimedia.org/api/rest_v1/media/math/render/svg/60335de80f83f077054c31e7ae187e819a01ca96) ,

which defines families of initial and terminal morphisms, in the following steps:

![{\displaystyle {\begin{aligned}\Phi _{Y,X}(f)=G(f)\circ \eta _{Y}\\\Phi _{Y,X}^{-1}(g)=\varepsilon _{X}\circ F(g)\end{aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/1faea6e8d082c2fcd78598e0e11d5ef0c4052db5)

for each *f*: *FY* → *X* and *g*: *Y* → *GX* (which completely determine Φ).

-   Substituting *FY* for *X* and η*Y* = Φ*Y*, *FY*(1*FY*) for *g* in the second formula gives the first counit–unit equation

![{\displaystyle 1_{FY}=\varepsilon _{FY}\circ F(\eta _{Y})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/18adf316799c31c12597d9c1f1e6aa77b66f772c),

and substituting *GX* for *Y* and εX = Φ−1*GX, X*(1*GX*) for *f* in the first formula gives the second counit–unit equation

![{\displaystyle 1_{GX}=G(\varepsilon _{X})\circ \eta _{GX}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/aa5f9da344f725ab1bbf0f24488cdf77a8d1447c).

Not every functor *G* : *C* → *D* admits a left adjoint. If *C* is a [complete category](https://en.wikipedia.org/wiki/Complete_category "Complete category"), then the functors with left adjoints can be characterized by the **adjoint functor theorem** of [Peter J. Freyd](https://en.wikipedia.org/wiki/Peter_J._Freyd "Peter J. Freyd"): *G* has a left adjoint if and only if it is [continuous](https://en.wikipedia.org/wiki/Limit_(category_theory)#Preservation_of_limits "Limit (category theory)") and a certain smallness condition is satisfied: for every object *Y* of *D* there exists a family of morphisms

*f**i* : *Y* → *G*(*X**i*)

where the indices *i* come from a *set* I, not a *[proper class](https://en.wikipedia.org/wiki/Class_(set_theory) "Class (set theory)")*, such that every morphism

*h* : *Y* → *G*(*X*)

can be written as

*h* = *G*(*t*) ∘ *f**i*

for some *i* in I and some morphism

*t* : *X**i* → *X* ∈ *C*.

An analogous statement characterizes those functors with a right adjoint.

An important special case is that of [locally presentable categories](https://en.wikipedia.org/wiki/Locally_presentable_category "Locally presentable category"). If ![{\displaystyle F:C\to D}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d082755579fdc0f7d9daca655472d59e8347242d) is a functor between locally presentable categories, then

-   *F* has a right adjoint if and only if *F* preserves small colimits
-   *F* has a left adjoint if and only if *F* preserves small limits and is an [accessible functor](https://en.wikipedia.org/wiki/Accessible_functor "Accessible functor")

If the functor *F* : *D* → *C* has two right adjoints *G* and *G*′, then *G* and *G*′ are [naturally isomorphic](https://en.wikipedia.org/wiki/Natural_transformation "Natural transformation"). The same is true for left adjoints.

Conversely, if *F* is left adjoint to *G*, and *G* is naturally isomorphic to *G*′ then *F* is also left adjoint to *G*′. More generally, if 〈*F*, *G*, ε, η〉 is an adjunction (with counit–unit (ε,η)) and

σ : *F* → *F*′

τ : *G* → *G*′

are natural isomorphisms then 〈*F*′, *G*′, ε′, η′〉 is an adjunction where

![{\displaystyle {\begin{aligned}\eta '&=(\tau \ast \sigma )\circ \eta \\\varepsilon '&=\varepsilon \circ (\sigma ^{-1}\ast \tau ^{-1}).\end{aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f540f2c599c62818fb16f3455210a40e56517b2d)

Here ![{\displaystyle \circ }](https://wikimedia.org/api/rest_v1/media/math/render/svg/99add39d2b681e2de7ff62422c32704a05c7ec31) denotes vertical composition of natural transformations, and ![{\displaystyle \ast }](https://wikimedia.org/api/rest_v1/media/math/render/svg/f1858484bef51b1435c2b986c728a81788051803) denotes horizontal composition.

Adjunctions can be composed in a natural fashion. Specifically, if 〈*F*, *G*, ε, η〉 is an adjunction between *C* and *D* and 〈*F*′, *G*′, ε′, η′〉 is an adjunction between *D* and *E* then the functor

![{\displaystyle F\circ F':E\rightarrow C}](https://wikimedia.org/api/rest_v1/media/math/render/svg/91dd6ef35b9bb75580d188db44524dd21cbbfb96)

is left adjoint to

![{\displaystyle G'\circ G:C\to E.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/00461ca3d02e9a9bd2c0d8ef13623de8704f83bb)

More precisely, there is an adjunction between *F F'* and *G' G* with unit and counit given respectively by the compositions:

![{\displaystyle {\begin{aligned}&1_{\mathcal {E}}{\xrightarrow {\eta '}}G'F'{\xrightarrow {G'\eta F'}}G'GFF'\\&FF'G'G{\xrightarrow {F\varepsilon 'G}}FG{\xrightarrow {\varepsilon }}1_{\mathcal {C}}.\end{aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/955277d076e8a9876aac5e3c422cd2dc047e1ec5)

This new adjunction is called the **composition** of the two given adjunctions.

Since there is also a natural way to define an identity adjunction between a category *C* and itself, one can then form a category whose objects are all [small categories](https://en.wikipedia.org/wiki/Small_category "Small category") and whose morphisms are adjunctions.

The most important property of adjoints is their continuity: every functor that has a left adjoint (and therefore *is* a right adjoint) is *continuous* (i.e. commutes with [limits](https://en.wikipedia.org/wiki/Limit_(category_theory) "Limit (category theory)") in the category theoretical sense); every functor that has a right adjoint (and therefore *is* a left adjoint) is *cocontinuous* (i.e. commutes with [colimits](https://en.wikipedia.org/wiki/Limit_(category_theory) "Limit (category theory)")).

Since many common constructions in mathematics are limits or colimits, this provides a wealth of information. For example:

-   applying a right adjoint functor to a [product](https://en.wikipedia.org/wiki/Product_(category_theory) "Product (category theory)") of objects yields the product of the images;
-   applying a left adjoint functor to a [coproduct](https://en.wikipedia.org/wiki/Coproduct "Coproduct") of objects yields the coproduct of the images;
-   every right adjoint functor between two abelian categories is [left exact](https://en.wikipedia.org/wiki/Left_exact_functor "Left exact functor");
-   every left adjoint functor between two abelian categories is [right exact](https://en.wikipedia.org/wiki/Right_exact_functor "Right exact functor").

If *C* and *D* are [preadditive categories](https://en.wikipedia.org/wiki/Preadditive_categories "Preadditive categories") and *F* : *D* → *C* is an [additive functor](https://en.wikipedia.org/wiki/Additive_functor "Additive functor") with a right adjoint *G* : *C* → *D*, then *G* is also an additive functor and the hom-set bijections

![{\displaystyle \Phi _{Y,X}:\mathrm {hom} _{\mathcal {C}}(FY,X)\cong \mathrm {hom} _{\mathcal {D}}(Y,GX)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d756dd4dec0f0ad3950c92e882db6b3cb00128c4)

are, in fact, isomorphisms of abelian groups. Dually, if *G* is additive with a left adjoint *F*, then *F* is also additive.

Moreover, if both *C* and *D* are [additive categories](https://en.wikipedia.org/wiki/Additive_categories "Additive categories") (i.e. preadditive categories with all finite [biproducts](https://en.wikipedia.org/wiki/Biproduct "Biproduct")), then any pair of adjoint functors between them are automatically additive.

### Universal constructions

\[[edit](https://en.wikipedia.org/w/index.php?title=Adjoint_functors&action=edit&section=34 "Edit section: Universal constructions")\]

As stated earlier, an adjunction between categories *C* and *D* gives rise to a family of [universal morphisms](https://en.wikipedia.org/wiki/Universal_morphism "Universal morphism"), one for each object in *C* and one for each object in *D*. Conversely, if there exists a universal morphism to a functor *G* : *C* → *D* from every object of *D*, then *G* has a left adjoint.

However, universal constructions are more general than adjoint functors: a universal construction is like an optimization problem; it gives rise to an adjoint pair if and only if this problem has a solution for every object of *D* (equivalently, every object of *C*).

### Equivalences of categories

\[[edit](https://en.wikipedia.org/w/index.php?title=Adjoint_functors&action=edit&section=35 "Edit section: Equivalences of categories")\]

If a functor *F* : *D* → *C* is one half of an [equivalence of categories](https://en.wikipedia.org/wiki/Equivalence_of_categories "Equivalence of categories") then it is the left adjoint in an adjoint equivalence of categories, i.e. an adjunction whose unit and counit are isomorphisms.

Every adjunction 〈*F*, *G*, ε, η〉 extends an equivalence of certain subcategories. Define *C*1 as the full subcategory of *C* consisting of those objects *X* of *C* for which ε*X* is an isomorphism, and define *D*1 as the [full subcategory](https://en.wikipedia.org/wiki/Full_subcategory "Full subcategory") of *D* consisting of those objects *Y* of *D* for which η*Y* is an isomorphism. Then *F* and *G* can be restricted to *D*1 and *C*1 and yield inverse equivalences of these subcategories.

In a sense, then, adjoints are "generalized" inverses. Note however that a right inverse of *F* (i.e. a functor *G* such that *FG* is naturally isomorphic to 1*D*) need not be a right (or left) adjoint of *F*. Adjoints generalize *two-sided* inverses.

Every adjunction 〈*F*, *G*, ε, η〉 gives rise to an associated [monad](https://en.wikipedia.org/wiki/Monad_(category_theory) "Monad (category theory)") 〈*T*, η, μ〉 in the category *D*. The functor

![{\displaystyle T:{\mathcal {D}}\to {\mathcal {D}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/041111697670704d5375f0fc1aa0860e2c99809a)

is given by *T* = *GF*. The unit of the monad

![{\displaystyle \eta :1_{\mathcal {D}}\to T}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d2b3103da86361357d674270099720f9a6046bf7)

is just the unit η of the adjunction and the multiplication transformation

![{\displaystyle \mu :T^{2}\to T\,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/80a6c3872b2a360514b157653de7db0e578c7d9a)

is given by μ = *G*ε*F*. Dually, the triple 〈*FG*, ε, *F*η*G*〉 defines a [comonad](https://en.wikipedia.org/wiki/Comonad "Comonad") in *C*.

Every monad arises from some adjunction—in fact, typically from many adjunctions—in the above fashion. Two constructions, called the category of [Eilenberg–Moore algebras](https://en.wikipedia.org/wiki/Eilenberg%E2%80%93Moore_algebra "Eilenberg–Moore algebra") and the [Kleisli category](https://en.wikipedia.org/wiki/Kleisli_category "Kleisli category") are two extremal solutions to the problem of constructing an adjunction that gives rise to a given monad.

1.  **[^](#cite_ref-1 "Jump up")** Baez, John C. (1996). "Higher-Dimensional Algebra II: 2-Hilbert Spaces". [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier) "ArXiv (identifier)"):[q-alg/9609018](https://arxiv.org/abs/q-alg/9609018).
2.  **[^](#cite_ref-2 "Jump up")** Kan, Daniel M. (1958). ["Adjoint Functors"](https://www.ams.org/journals/tran/1958-087-02/S0002-9947-1958-0131451-0/S0002-9947-1958-0131451-0.pdf) (PDF). *[Transactions of the American Mathematical Society](https://en.wikipedia.org/wiki/Transactions_of_the_American_Mathematical_Society "Transactions of the American Mathematical Society")*. **87** (2): 294–329. [doi](https://en.wikipedia.org/wiki/Doi_(identifier) "Doi (identifier)"):[10.2307/1993102](https://doi.org/10.2307%2F1993102). [JSTOR](https://en.wikipedia.org/wiki/JSTOR_(identifier) "JSTOR (identifier)") [1993102](https://www.jstor.org/stable/1993102).
3.  **[^](#cite_ref-3 "Jump up")** [Lawvere, F. William](https://en.wikipedia.org/wiki/William_Lawvere "William Lawvere"), "[Adjointness in foundations](http://www.tac.mta.ca/tac/reprints/articles/16/tr16abs.html)", *Dialectica*, 1969. The notation is different nowadays; an easier introduction by Peter Smith [in these lecture notes](http://www.logicmatters.net/resources/pdfs/Galois.pdf), which also attribute the concept to the article cited.
4.  **[^](#cite_ref-4 "Jump up")** ["Indiscrete category"](http://ncatlab.org/nlab/show/indiscrete+category). *nLab*.
5.  **[^](#cite_ref-5 "Jump up")** [Mac Lane, Saunders](https://en.wikipedia.org/wiki/Saunders_Mac_Lane "Saunders Mac Lane"); Moerdijk, Ieke (1992) *Sheaves in Geometry and Logic*, Springer-Verlag. [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier) "ISBN (identifier)") [0-387-97710-4](https://en.wikipedia.org/wiki/Special:BookSources/0-387-97710-4 "Special:BookSources/0-387-97710-4") *See page 58*

-   Adámek, Jiří; Herrlich, Horst; Strecker, George E. (1990). [*Abstract and Concrete Categories. The joy of cats*](http://katmat.math.uni-bremen.de/acc/acc.pdf) (PDF). John Wiley & Sons. [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier) "ISBN (identifier)") [0-471-60922-6](https://en.wikipedia.org/wiki/Special:BookSources/0-471-60922-6 "Special:BookSources/0-471-60922-6"). [Zbl](https://en.wikipedia.org/wiki/Zbl_(identifier) "Zbl (identifier)") [0695.18001](https://zbmath.org/?format=complete&q=an:0695.18001).
-   [Mac Lane, Saunders](https://en.wikipedia.org/wiki/Saunders_Mac_Lane "Saunders Mac Lane") (1998). *[Categories for the Working Mathematician](https://en.wikipedia.org/wiki/Categories_for_the_Working_Mathematician "Categories for the Working Mathematician")*. [Graduate Texts in Mathematics](https://en.wikipedia.org/wiki/Graduate_Texts_in_Mathematics "Graduate Texts in Mathematics"). Vol. 5 (2nd ed.). Springer-Verlag. [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier) "ISBN (identifier)") [0-387-98403-8](https://en.wikipedia.org/wiki/Special:BookSources/0-387-98403-8 "Special:BookSources/0-387-98403-8"). [Zbl](https://en.wikipedia.org/wiki/Zbl_(identifier) "Zbl (identifier)") [0906.18001](https://zbmath.org/?format=complete&q=an:0906.18001).

-   [Adjunctions](https://www.youtube.com/playlist?list=PL54B49729E5102248) playlist on [YouTube](https://en.wikipedia.org/wiki/YouTube_playlist_(identifier) "YouTube playlist (identifier)") – seven short lectures on adjunctions by [Eugenia Cheng](https://en.wikipedia.org/wiki/Eugenia_Cheng "Eugenia Cheng") of The Catsters
-   [WildCats](http://wildcatsformma.wordpress.com/) is a category theory package for [Mathematica](https://en.wikipedia.org/wiki/Mathematica "Mathematica"). Manipulation and visualization of objects, [morphisms](https://en.wikipedia.org/wiki/Morphism "Morphism"), categories, [functors](https://en.wikipedia.org/wiki/Functor "Functor"), [natural transformations](https://en.wikipedia.org/wiki/Natural_transformation "Natural transformation"), [universal properties](https://en.wikipedia.org/wiki/Universal_properties "Universal properties").