"""Tests for skill restructuring to nw-prefixed SKILL.md format.

Step 01-02: Restructure 3 troubleshooter skills (pilot).
Step 02-01: Restructure all 127 non-colliding skills (bulk migration).
"""

from pathlib import Path

import pytest


SKILLS_DIR = Path(__file__).resolve().parents[3] / "nWave" / "skills"

EXPECTED_TROUBLESHOOTER_SKILLS = [
    "nw-five-whys-methodology",
    "nw-investigation-techniques",
    "nw-post-mortem-framework",
]

# Content hashes captured before restructuring (md5)
TROUBLESHOOTER_HASHES = {
    "nw-five-whys-methodology": "25502cf312b262bc635eeb40ada7469b",
    "nw-investigation-techniques": "156f0cb3e13a2abc4f100bbfdb23326d",
    "nw-post-mortem-framework": "ae5059d83ca42ff1004040d3090c7a30",
}

# Step 02-01: All 127 non-colliding skills to migrate (bulk)
# Excludes: critique-dimensions (7), review-criteria (7), review-dimensions (2)
EXPECTED_BULK_SKILLS = [
    "nw-agent-creation-workflow",
    "nw-agent-testing",
    "nw-ai-workflow-tutorials",
    "nw-architectural-styles-tradeoffs",
    "nw-architecture-patterns",
    "nw-assessment-kirkpatrick",
    "nw-authoritative-sources",
    "nw-backward-design-ubd",
    "nw-bdd-methodology",
    "nw-bdd-requirements",
    "nw-cialdini-outreach",
    "nw-cicd-and-deployment",
    "nw-cognitive-load-management",
    "nw-cognitive-load-theory",
    "nw-collaboration-and-handoffs",
    "nw-collapse-detection",
    "nw-command-design-patterns",
    "nw-command-optimization-workflow",
    "nw-competitive-analysis",
    "nw-compliance-framework",
    "nw-copy-paste-quality",
    "nw-copywriting-frameworks",
    "nw-css-implementation-recipes",
    "nw-curriculum-series-design",
    "nw-data-architecture-patterns",
    "nw-data-source-catalog",
    "nw-database-technology-selection",
    "nw-deliver-orchestration",
    "nw-deployment-strategies",
    "nw-design-methodology",
    "nw-design-patterns",
    "nw-discovery-methodology",
    "nw-discovery-workflow",
    "nw-divio-framework",
    "nw-domain-driven-design",
    "nw-dor-validation",
    "nw-dossier-templates",
    "nw-entity-resolution",
    "nw-fisher-ury-preparation",
    "nw-formal-verification-tlaplus",
    "nw-fp-algebra-driven-design",
    "nw-fp-clojure",
    "nw-fp-domain-modeling",
    "nw-fp-fsharp",
    "nw-fp-haskell",
    "nw-fp-hexagonal-architecture",
    "nw-fp-kotlin",
    "nw-fp-principles",
    "nw-fp-scala",
    "nw-fp-usable-design",
    "nw-futuristic-color-typography",
    "nw-gamification-mda-wow-aha",
    "nw-hexagonal-testing",
    "nw-icp-design",
    "nw-infrastructure-and-observability",
    "nw-interaction-choreography",
    "nw-interviewing-techniques",
    "nw-it-specific-pedagogy",
    "nw-jtbd-bdd-integration",
    "nw-jtbd-core",
    "nw-jtbd-interviews",
    "nw-jtbd-opportunity-scoring",
    "nw-jtbd-workflow-selection",
    "nw-lean-canvas-methodology",
    "nw-leanux-methodology",
    "nw-legacy-refactoring-ddd",
    "nw-liberating-structures-facilitation",
    "nw-mikado-method",
    "nw-neuroscience-learning",
    "nw-online-facilitation-miro-boards",
    "nw-operational-safety",
    "nw-opportunity-mapping",
    "nw-outcome-kpi-framework",
    "nw-pbt-dotnet",
    "nw-pbt-erlang-elixir",
    "nw-pbt-fundamentals",
    "nw-pbt-go",
    "nw-pbt-haskell",
    "nw-pbt-jvm",
    "nw-pbt-python",
    "nw-pbt-rust",
    "nw-pbt-stateful",
    "nw-pbt-typescript",
    "nw-pedagogy-bloom-andragogy",
    "nw-persona-jtbd-analysis",
    "nw-platform-engineering-foundations",
    "nw-pricing-frameworks",
    "nw-production-readiness",
    "nw-production-safety",
    "nw-progressive-refactoring",
    "nw-property-based-testing",
    "nw-proposal-structure",
    "nw-psychological-safety",
    "nw-quality-framework",
    "nw-quality-validation",
    "nw-query-optimization",
    "nw-research-methodology",
    "nw-review-output-format",
    "nw-review-workflow",
    "nw-roadmap-design",
    "nw-roadmap-review-checks",
    "nw-sci-fi-design-patterns",
    "nw-security-and-governance",
    "nw-security-by-design",
    "nw-sequence-design",
    "nw-shared-artifact-tracking",
    "nw-signal-detection",
    "nw-source-verification",
    "nw-stakeholder-engagement",
    "nw-stress-analysis",
    "nw-tbr-methodology",
    "nw-tdd-methodology",
    "nw-tdd-review-enforcement",
    "nw-test-design-mandates",
    "nw-test-organization-conventions",
    "nw-test-refactoring-catalog",
    "nw-tlaplus-verification",
    "nw-tutorial-structure",
    "nw-usability-engineering",
    "nw-user-story-mapping",
    "nw-ux-desktop-patterns",
    "nw-ux-emotional-design",
    "nw-ux-principles",
    "nw-ux-tui-patterns",
    "nw-ux-web-patterns",
    "nw-voss-negotiation",
    "nw-wizard-shared-rules",
]

BULK_HASHES = {
    "nw-ab-critique-dimensions": "73bd1bd637a3abb8b639d8eebb2a012c",
    "nw-abr-critique-dimensions": "1fe367e9401c076445dae5c196ffb9b4",
    "nw-ad-critique-dimensions": "469727a8ff5b9ef61e05d6230c9f04a2",
    "nw-agent-creation-workflow": "6b748c11fe1edae64271d41a8c5747fc",
    "nw-agent-testing": "08e8d015be3670f8f15ab420cb6b3f1b",
    "nw-ai-workflow-tutorials": "1cc2f6e4481d76d50c1df7839068d298",
    "nw-architectural-styles-tradeoffs": "cf9ed1b8b83987e437a87167e25f9a32",
    "nw-architecture-patterns": "d296d25e56298815be4723ac8abdabed",
    "nw-assessment-kirkpatrick": "7e57f3ae01d4667516d8f911e6e35ac6",
    "nw-authoritative-sources": "235291357257333c9897aac22f5c4188",
    "nw-backward-design-ubd": "e73d2c89d938b9159eb2aecb472f405d",
    "nw-bdd-methodology": "40191b34da63f9ba79f82217cc913ce5",
    "nw-bdd-requirements": "940b444d8036d5422516791b9ec445e3",
    "nw-br-review-criteria": "3aceddccd79d0d4c73083645900dbe3b",
    "nw-canary": "165934de1756fbb81ce45e69e0202e8d",
    "nw-cialdini-outreach": "f40e9ec0b2eb19b3246ef26ae8b1af15",
    "nw-cicd-and-deployment": "b53e0dc1a3a1fd1d69030de7d922e8c8",
    "nw-cognitive-load-management": "907f81bf3456bac2eff68adba98111ff",
    "nw-cognitive-load-theory": "45127937413e558aeb79347febf3900f",
    "nw-collaboration-and-handoffs": "2a3414c82033aeed807243072ddb36be",
    "nw-collapse-detection": "4f56406bbcd03dd8842d030f3ea02286",
    "nw-command-design-patterns": "30e8e910529297ea0754a5a8a746534a",
    "nw-command-optimization-workflow": "30bcd47ba360775d031f24803a171d13",
    "nw-competitive-analysis": "c437d62c7226812efa67676b5d960204",
    "nw-compliance-framework": "94cc86b7e0e47dac89c61354067a9b41",
    "nw-copy-paste-quality": "3c7a22afbec45cf802a95fde1db97813",
    "nw-copywriting-frameworks": "46d31598ec7aa0de0f7acea53ac247f9",
    "nw-css-implementation-recipes": "571564e89a4d88ef0f23bcd6ef02e1ed",
    "nw-curriculum-series-design": "5a9ab50585ad2fa348293e661d9ae1ac",
    "nw-data-architecture-patterns": "7a435d0ab5c135191f4ac63588b2800d",
    "nw-data-source-catalog": "37e3d10bf5c99aef4d2f65c15c95978b",
    "nw-database-technology-selection": "ff06a5bf3f7387881078458214ee5bdc",
    "nw-deliver-orchestration": "508e8f0f8ad65ee10d2f06ba736ebbe9",
    "nw-deployment-strategies": "f5e53a35b530d65ffa4e5a535dd14913",
    "nw-der-review-criteria": "88836eb6d187e41ef5b6d5b31e00fb2a",
    "nw-design-methodology": "67bfcda8b6bb2cd2a9507cecf5e3dd77",
    "nw-design-patterns": "8385077a13ffde8d6ce619ab17e0dc66",
    "nw-discovery-methodology": "5df256af28a369c419a2067d8546d144",
    "nw-discovery-workflow": "47fa0608166d2fbc9fb83c10ee94c0d7",
    "nw-divio-framework": "39d19325db3d4b02b23164a1da12fc50",
    "nw-domain-driven-design": "77f661c5c17c9f90ac88162a874de3bd",
    "nw-dor-validation": "330b7390693cc94f75e3b5fca673791f",
    "nw-dossier-templates": "835fc5ae62be9dfd5e2ebd32e0962031",
    "nw-dr-review-criteria": "cc44d7d23c0996ac5e0d7e3be3e1a6a4",
    "nw-entity-resolution": "e912e851be549dc6dc250400808ac221",
    "nw-fisher-ury-preparation": "0dc1808ba8c70baafc89f419a263f91c",
    "nw-five-whys-methodology": "25502cf312b262bc635eeb40ada7469b",
    "nw-formal-verification-tlaplus": "ce345dee30069e081b54fcc614585d57",
    "nw-fp-algebra-driven-design": "11bda52c215f7580d13e80e335b9afd6",
    "nw-fp-clojure": "a872950514a2a54616ab2df9ef8e8230",
    "nw-fp-domain-modeling": "0d94280a5ba1cb1c69ae97c7785605ba",
    "nw-fp-fsharp": "735225df00c248cf90ad91baf95b7ac3",
    "nw-fp-haskell": "bf83c94800c8467e3f392414a3523591",
    "nw-fp-hexagonal-architecture": "c4ce3240bf4e5a1352d19d5ad6d62f58",
    "nw-fp-kotlin": "7fb88e1185cec839df66a3cd6026a994",
    "nw-fp-principles": "743a4d91b50d207cbcce114b1284554b",
    "nw-fp-scala": "6d40d5e9a7e1658de4b2b205418e77fa",
    "nw-fp-usable-design": "f26cfc02b0e6d76044759b5e9a2c9419",
    "nw-futuristic-color-typography": "a70566514dbd76d7eae7589a95904acd",
    "nw-gamification-mda-wow-aha": "67154664b53f70bd1312d23de85edbf7",
    "nw-hexagonal-testing": "9b2c2620ac34a142a01cacdf575d254c",
    "nw-icp-design": "c036359cefd7dff27638c2cb49f44204",
    "nw-infrastructure-and-observability": "c025f9e61e0043790defabfff7bc16b8",
    "nw-interaction-choreography": "225097c35233f6422d74e47f2f420e5a",
    "nw-interviewing-techniques": "0b0bc30ce3697d3833ab00248039e586",
    "nw-investigation-techniques": "156f0cb3e13a2abc4f100bbfdb23326d",
    "nw-it-specific-pedagogy": "c344c78a11db2f324eb17bec24f381fb",
    "nw-jtbd-bdd-integration": "23d023facd5649e61ef59454c3895000",
    "nw-jtbd-core": "272ae18df283a764f1089366d5fcc123",
    "nw-jtbd-interviews": "124e3d2c4c27846eac51bb503b5f8cf6",
    "nw-jtbd-opportunity-scoring": "b69671f2956e9a0a5faff8a0bbcb8ed3",
    "nw-jtbd-workflow-selection": "48a7394fc21ba62ca46220d2095bdd39",
    "nw-lean-canvas-methodology": "1322e95e6e5e0a143f74b45c8b5ef001",
    "nw-leanux-methodology": "3ff3121a7d77fc8bc6fb5a5959f2e931",
    "nw-legacy-refactoring-ddd": "2ac35af0580842c8e18ec17bb7ae9de9",
    "nw-liberating-structures-facilitation": "eb9da07234ed5279700c55c475095f95",
    "nw-mikado-method": "0adb7455087efecf8584cd4d66526e2d",
    "nw-neuroscience-learning": "7430f3af6926628f08df0259f92c2803",
    "nw-online-facilitation-miro-boards": "367c975639ba77b122c45f1de8198c9d",
    "nw-operational-safety": "f640a1a19b8cb391a87c32105f0fd51b",
    "nw-opportunity-mapping": "3f0be27f4f312e8d85aa1b0ee6d4336b",
    "nw-outcome-kpi-framework": "3fd36b1905c08439de22506025b1426d",
    "nw-par-critique-dimensions": "184b9db4511f64a5b3e3336b2f59df79",
    "nw-par-review-criteria": "d3b48298d6a97238b9be7d2ad00688d3",
    "nw-pbt-dotnet": "1487c97d51f2224689ab02e14bad481b",
    "nw-pbt-erlang-elixir": "d6fa697354f746fde1f3c19c2e8bf833",
    "nw-pbt-fundamentals": "336aadfa250fa56b48fea81b8014ddad",
    "nw-pbt-go": "3a79daf10fefdd6edffd6005977a06c2",
    "nw-pbt-haskell": "2594a614becb626fed4d6459a187b105",
    "nw-pbt-jvm": "a1d09166128ca1966d5a6911d7c238f9",
    "nw-pbt-python": "54d535a53ef3392c433f129962852f2d",
    "nw-pbt-rust": "9efb17415c7a8423685d9b7b3153ddf7",
    "nw-pbt-stateful": "697b963fd8355c380c2b2f0c51b8fe74",
    "nw-pbt-typescript": "ae741b2ab4cd3bc5aab6782233b6e7cd",
    "nw-pdr-review-criteria": "d8200b18255a8302efa0ce53852e86f3",
    "nw-pedagogy-bloom-andragogy": "ed17028d798e2304fece753c2f2459bd",
    "nw-persona-jtbd-analysis": "6641658fb69ff397bcf101b727a85246",
    "nw-platform-engineering-foundations": "cd9be53f591e441828f25a86f1c8a207",
    "nw-po-review-dimensions": "9d70cec700a983ee3f78e0da1039b164",
    "nw-por-review-criteria": "32e837f1539c9d45e225659426d54514",
    "nw-post-mortem-framework": "ae5059d83ca42ff1004040d3090c7a30",
    "nw-pricing-frameworks": "8083f7f279ca76274e21082702773dfa",
    "nw-production-readiness": "10677d8e3de793fe59cdfaf798cddc1b",
    "nw-production-safety": "9fc2a831470047fc8a3ca4c9a1ee62aa",
    "nw-progressive-refactoring": "441efe908c713c570e58c2f9a8e74abb",
    "nw-property-based-testing": "f9b60c6b08ab5b007a43026be47c1afc",
    "nw-proposal-structure": "4356636952f216f9764311dcb5f7b5ad",
    "nw-psychological-safety": "bd3d31727ba7798d97a0c740363888dc",
    "nw-quality-framework": "123c35e6b3e79a6467c18c1c3005d80b",
    "nw-quality-validation": "2c8bba01338c12895ce89c68b6f52997",
    "nw-query-optimization": "4053c6312888eb8eeabd74f9b3cd3286",
    "nw-research-methodology": "7d4422cd806919e512ad87dd92848c96",
    "nw-review-output-format": "7d01a939be71455b31bb5b02f5b16a74",
    "nw-review-workflow": "aa4c78c081af286baa12d066267e5657",
    "nw-roadmap-design": "f053503dd0668f1a306767d96208c668",
    "nw-roadmap-review-checks": "b1fa5a18665a3ba558b2d1e0574c4a5a",
    "nw-rr-critique-dimensions": "daa2cc2de681f442bff04f5b1a8ca8b9",
    "nw-sa-critique-dimensions": "5052e8ddbb4e8d65fe11bac25dcfbd6e",
    "nw-sar-critique-dimensions": "eb728e45a30e814cecc6ccebfb3bde36",
    "nw-sc-review-dimensions": "50d40ae0c8ce3eb81df31c892c27d37b",
    "nw-sci-fi-design-patterns": "e7f31312b385b928b466c655a597f65c",
    "nw-security-and-governance": "4161e1517da1279a4690a713b28650b9",
    "nw-security-by-design": "5fc0ac54b885e6e967534f3e37edecdb",
    "nw-sequence-design": "fbe03c8bf12046e1871e4eb59738e8b3",
    "nw-shared-artifact-tracking": "f9006e4ad490a413fc57b75ae536ab9a",
    "nw-signal-detection": "f7d58df32bac06706a165dc33762f5c2",
    "nw-source-verification": "e403c6ada295d30b8baee3a2be960820",
    "nw-stakeholder-engagement": "5fc54d0262152b29bfe462e3e946b531",
    "nw-stress-analysis": "fc88a57c7d4a272bf54545e018ca5a63",
    "nw-tbr-methodology": "2d5244d94e7f13618708c7010d3a5473",
    "nw-tdd-methodology": "b3cf26264d7c0bb58c6e0e3cb08c8407",
    "nw-tdd-review-enforcement": "d92313308bdef04b47ea786b08dc8657",
    "nw-test-design-mandates": "36d41aa8aa43b21bd248c50f1a5a1f0e",
    "nw-test-organization-conventions": "e90c46fd54357a06d5480437a3adae01",
    "nw-test-refactoring-catalog": "1102248431fd38fd2f9b85377dbc47fa",
    "nw-tlaplus-verification": "a652886c88d1820dd7af49f639f09ffb",
    "nw-tr-review-criteria": "e53e2aec4e69df2c39a34f226b6a2568",
    "nw-tutorial-structure": "9d2986344b069807f745bf9c6da63e62",
    "nw-usability-engineering": "ee06d1ab6123eaf123a0483b6eb17f45",
    "nw-user-story-mapping": "7cbd33bebdcc74c70af527b6a805fc1a",
    "nw-ux-desktop-patterns": "933ae86a0cf4ac76c89d473dc8dbbc79",
    "nw-ux-emotional-design": "2194868543d80c8078c12bb6103467f3",
    "nw-ux-principles": "e531e440abb7c90287aef1c0e2292b7d",
    "nw-ux-tui-patterns": "f85c36f87c09360ec5c1f8c209e71f1d",
    "nw-ux-web-patterns": "bf237cc9b015c458df3d1e21513c4d0b",
    "nw-voss-negotiation": "c1fe20f47266d48c1623df00444dae8d",
    "nw-wizard-shared-rules": "b50b0b424a014f3e45adf0b2db140de3",
}

# Agent directories that should be fully emptied after migration
# (all their skills are non-colliding and will be moved)
FULLY_EMPTIED_AGENT_DIRS = [
    "business-discoverer",
    "business-osint",
    "common",
    "data-engineer",
    "deal-closer",
    "documentarist",
    "functional-software-crafter",
    "outreach-writer",
    "platform-architect",
    "product-discoverer",
    "researcher",
    "software-crafter-reviewer",
    "tutorialist",
    "ux-designer",
    "workshopper",
]


class TestTroubleshooterSkillRestructuring:
    """Step 01-02: Verify troubleshooter skills are restructured."""

    @pytest.mark.parametrize("skill_name", EXPECTED_TROUBLESHOOTER_SKILLS)
    def test_skill_directory_exists_with_skill_md(self, skill_name: str) -> None:
        """Each troubleshooter skill must exist as nw-{name}/SKILL.md."""
        skill_file = SKILLS_DIR / skill_name / "SKILL.md"
        assert skill_file.exists(), (
            f"Expected {skill_file.relative_to(SKILLS_DIR)} to exist"
        )

    @pytest.mark.parametrize("skill_name", EXPECTED_TROUBLESHOOTER_SKILLS)
    def test_skill_content_preserved(self, skill_name: str) -> None:
        """Content must be identical to original after restructuring."""
        import hashlib

        skill_file = SKILLS_DIR / skill_name / "SKILL.md"
        if not skill_file.exists():
            pytest.skip(f"{skill_name}/SKILL.md does not exist yet")

        content = skill_file.read_bytes()
        actual_hash = hashlib.md5(content).hexdigest()
        assert actual_hash == TROUBLESHOOTER_HASHES[skill_name], (
            f"Content hash mismatch for {skill_name}: "
            f"expected {TROUBLESHOOTER_HASHES[skill_name]}, got {actual_hash}"
        )

    def test_old_troubleshooter_directory_removed(self) -> None:
        """The old agent-grouped troubleshooter/ directory should not contain
        the migrated files."""
        old_dir = SKILLS_DIR / "troubleshooter"
        old_files = [
            "five-whys-methodology.md",
            "investigation-techniques.md",
            "post-mortem-framework.md",
        ]
        for filename in old_files:
            old_file = old_dir / filename
            assert not old_file.exists(), (
                f"Old file {old_file.relative_to(SKILLS_DIR)} should have been moved"
            )


class TestBulkSkillRestructuring:
    """Step 02-01: Verify all 127 non-colliding skills are restructured to
    nw-prefixed SKILL.md format."""

    @pytest.mark.parametrize("skill_name", EXPECTED_BULK_SKILLS)
    def test_skill_directory_exists_with_skill_md(self, skill_name: str) -> None:
        """Each non-colliding skill must exist as nw-{name}/SKILL.md."""
        skill_file = SKILLS_DIR / skill_name / "SKILL.md"
        assert skill_file.exists(), (
            f"Expected {skill_file.relative_to(SKILLS_DIR)} to exist"
        )

    def test_total_nw_prefixed_skill_count(self) -> None:
        """Total nw-* directories should be 130 (127 bulk + 3 troubleshooter)."""
        nw_dirs = sorted(
            d for d in SKILLS_DIR.iterdir() if d.is_dir() and d.name.startswith("nw-")
        )
        skill_dirs_with_md = [d for d in nw_dirs if (d / "SKILL.md").exists()]
        assert len(skill_dirs_with_md) >= 130, (
            f"Expected >= 130 nw-*/SKILL.md directories, found {len(skill_dirs_with_md)}"
        )

    @pytest.mark.parametrize("skill_name", EXPECTED_BULK_SKILLS)
    def test_skill_content_preserved(self, skill_name: str) -> None:
        """Content must be identical to original after restructuring."""
        import hashlib

        skill_file = SKILLS_DIR / skill_name / "SKILL.md"
        if not skill_file.exists():
            pytest.skip(f"{skill_name}/SKILL.md does not exist yet")

        content = skill_file.read_bytes()
        actual_hash = hashlib.md5(content).hexdigest()
        assert actual_hash == BULK_HASHES[skill_name], (
            f"Content hash mismatch for {skill_name}: "
            f"expected {BULK_HASHES[skill_name]}, got {actual_hash}"
        )

    @pytest.mark.parametrize("agent_dir", FULLY_EMPTIED_AGENT_DIRS)
    def test_fully_emptied_agent_directories_removed(self, agent_dir: str) -> None:
        """Agent directories with only non-colliding skills should be removed."""
        old_dir = SKILLS_DIR / agent_dir
        assert not old_dir.exists(), (
            f"Old directory {agent_dir}/ should have been removed after migration"
        )
