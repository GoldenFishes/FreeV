### Reviewer #1

#### Questions

- 1. Paper Summary. In a few sentences, describe the key ideas, results, findings, and significance as claimed by the paper’s authors.

  - The paper applies FreeU, traditionally tested on convolution architectures, to transformer architectures like U-ViT. The paper identifies and visualizes differences between frequency responses after certain outputs between FreeU and U-ViT and proposes an additional modulation factor to account for these differences. Finally, it introduces two new sets of evaluation metrics that aim to identify the impact of multimodal capabilities.

- 2. Strengths. Consider, among others, the significance of critical ideas, validation, writing quality, and data contribution. Explain clearly why these aspects of the paper are valuable.

  - The paper provides good visualizations of the different frequency responses at different timesteps in the U-ViT architecture (similar to how FreeU does). The motivation to add a modulation factor f makes sense because the frequency response after fusion differs from FreeU.

- 3. Weaknesses. Clearly explain why these are weak aspects of the paper, e.g., why a specific prior work has already demonstrated the key contributions, why the experiments are insufficient to validate the claims, etc.

  - The application of FreeU to U-ViT represents a minor contribution. The primary novelty lies in applying FreeU to U-ViT and introducing the modulation factor f. However, the significance of factor f is unclear as Figure 6 suggests comparable performance even with a constant value for f. Although this approach holds potential, the paper lacks comprehensive experiments, such as aggregated results and user studies, to substantiate strong claims. Furthermore, the proposed evaluation metrics may contain methodological issues.

    The authors show qualitative and quantitative results on only 6-10 examples and do not run any aggregated statistics for results on a statistically significant number of images (e.g., on a test set of a dataset). Figure 11 shows the baseline UD outperforming their proposed FreeV in 5 out of the 6 results on their proposed IBT score. They justify this poor performance by stating “FreeV improves image quality” in line 680 without any quantitative or qualitative evidence to suggest that the image quality actually improved. Similarly, in Figure 12’s analysis, they state “FreeV’s advantage in text-to-image tasks is evident” without any basis in qualitative or quantitative results or any analysis. In Figure 12, UD outperforms FreeV in half the results on their proposed IBI score, also indicating questionable improvements over the baseline.

    The utility of the proposed metrics is questionable. For instance, the IBI score uses SSIM without any justification for its choice. In fact, going from image to text and then back from text to image without any guidance on structure would undoubtedly lead to generations with very different structures—likely leading to very low SSIM scores. This can be verified in Figure 12, where the SSIM scores are between 0.05 and 0.1, indicating SSIM may not be an appropriate metric to be used in this scenario.

    Another example of inadequate analysis is shown on line 757, where the authors state that “it is natural to conclude that this modified method does not perform well in non-Text2Vision generation tasks”. The authors base their claim on the results from IBI, but IBI has clear flaws in its design using SSIM. Furthermore, the attribution of the error is unclear because the metric uses both text-to-image and image-to-text when calculating the score. How the authors conclude that “text-to-image” works but “image-to-text” does not is unclear.

    Finally, the authors lack user studies to support the effectiveness of their method and rely on poorly designed metrics to evaluate it. As metrics can often be inaccurate and “preference” between examples can be subjective, generative tasks benefit from conducting user studies (as FreeU does in their paper). With no user studies, only 6-10 qualitative examples, and no aggregated statistics, it’s hard to see a conclusive impact of FreeV.

    The paper has many typos and grammar mistakes (e.g. “5.1 The different experimental conclusion between we [sic] and FreeU” line 694, “More discussion of the motivationr [sic]”, etc.). Some paragraphs are difficult to understand (e.g. line 354-357 left column). The paper also states in line 175 that “directly transferring U-Net’s improvement methods from Free U to U-ViT didn’t yield significant effects”, but it is unclear where this conclusion comes from. Overall, the paper requires substantial revision to strengthen its claims, improve clarity, and eliminate typos.

- 4. Recommendation. Rate the paper as it stands now.

  - Strong Reject

- 5. Justification. Be specific: What are the most critical factors in your rating?

  - The application of FreeU to U-ViT alone is already a limited novel contribution. Without thorough experimentation and conclusive results, my recommendation is a strong reject.

- 6. Should the paper be invited for resubmission in the second WACV 2025 submission round if it is not already accepted in the first round? The invitation to resubmit implies that the paper can be made acceptable after some reasonable revisions.

  - No, the required revisions are too extensive for a resubmission in the time that is available.

### Reviewer #2

#### Questions

- 1. Paper Summary. In a few sentences, describe the key ideas, results, findings, and significance as claimed by the paper’s authors.

  - The paper explored the potential of using U-ViT as the backbone for transformer-based diffusion models. The key idea is to adjust the weights of features from the skip connections to boost the performance of underlying diffusion models without additional training.

- 2. Strengths. Consider, among others, the significance of critical ideas, validation, writing quality, and data contribution. Explain clearly why these aspects of the paper are valuable.

  - The experiments and findings are interesting. For example, how features from main model and skip connections at different frequencies contribute to the generated image at different denoising steps.

    The motivation is clear. Despite the outcome of the study, exploration of whether a simple feature-adjustment-based approach can be used for transformer-based diffusion can be useful.

- 3. Weaknesses. Clearly explain why these are weak aspects of the paper, e.g., why a specific prior work has already demonstrated the key contributions, why the experiments are insufficient to validate the claims, etc.

  - The structure of the paper follows the freeU [23] paper exactly, except that the main idea of neither freeV (in this paper) nor freeU [23] are clearly described. The current paper assumes that readers are very familiar with freeU [23], and directly jumps into freeV as a parallel approach of freeU. I strongly suggest the authors to modify the paper to make it clear why freeV or freeU is useful, how freeU works, etc.

    Apparently the benefit of the proposed freeV is not as obvious as freeU for U-Net-based diffusion models. For example, Fig.2 and 3 look much messier than the corresponding figures in [23]. The paper reports many findings, which are all over the place. It would be helpful to give a summary of the main findings in earlier part of the paper rather than in final discussions.

    Since the paper is based on the same idea of freeU, it would be better if the paper can compare with freeU on image generation directly, despite the different backbone structures.

- 4. Recommendation. Rate the paper as it stands now.

  - Borderline

- 5. Justification. Be specific: What are the most critical factors in your rating?

  - As stated above, I think the motivation is clear and the findings can be useful. However, I also think it is necessary to revise the paper to make it more clear, more readable, and more convincing.

- 6. Should the paper be invited for resubmission in the second WACV 2025 submission round if it is not already accepted in the first round? The invitation to resubmit implies that the paper can be made acceptable after some reasonable revisions.

  - Yes, the paper is of reasonable quality but requires some revisions before it can be accepted.

- 7. What are the main revisions that are needed to make the paper acceptable after the resubmission in the second round. [Applicable only if you recommended a resubmission of the paper in the previous question.]

  - Clear motivation of freeU or freeV
    Main findings: pros and cons, unique findings different from freeU
    Compare with freeU to prove the usefulness of freeV

### Reviewer #3

#### Questions

- 1. Paper Summary. In a few sentences, describe the key ideas, results, findings, and significance as claimed by the paper’s authors.

  - Based on the success of FreeU in Diffusion models, this paper proposes an improved method for the multimodal diffusion models, called "FreeV". The authors state that the proposed "Free V" can improve the generated quality.

- 2. Strengths. Consider, among others, the significance of critical ideas, validation, writing quality, and data contribution. Explain clearly why these aspects of the paper are valuable.

  - (-) The topic of this paper is interesting.

- 3. Weaknesses. Clearly explain why these are weak aspects of the paper, e.g., why a specific prior work has already demonstrated the key contributions, why the experiments are insufficient to validate the claims, etc.

  - (-) The motivation of this paper is not clear enough. The author states the success of FreeU in the existing studies but does not well explain the weakness of FreeU in the multimodal generation tasks. Furthermore, there is no further explanation of the difference between the proposed FreeV and FreeU.

    (-) There lack of formal experiment tables to report the results and a lack of commonly-used metrics, i.e., FID, in all experiments. Furthermore, to demonstrate the significance of the proposed FreeV, the authors should conduct experiments on different T2I methods.

    (-) The presentation of this paper is poor. Some examples are shown as follows.

    (1) Line 1 FreeU first time in the paper without explanation.

    (2) The color of Figure 2 is hard to recognize.

    (3) The text in Figures 4 to 10 is difficult to see.

- 4. Recommendation. Rate the paper as it stands now.

  - Weak Reject

- 5. Justification. Be specific: What are the most critical factors in your rating?

  - I think this paper is not ready to be published now and needs to be further improved.

- 6. Should the paper be invited for resubmission in the second WACV 2025 submission round if it is not already accepted in the first round? The invitation to resubmit implies that the paper can be made acceptable after some reasonable revisions.

  - No, the required revisions are too extensive for a resubmission in the time that is available.