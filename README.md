# ORE-MINECRAFT

Source-archive workspace for **42 Regolith Labs repositories**. This bootstrap commit contains the manifest, clone tooling, and a manual GitHub Actions workflow; it does **not** yet contain the 42 cloned source trees. Run the workflow to produce a source ZIP with provenance.

## 01-core-protocol

- [ore](https://github.com/regolith-labs/ore)
- [ore-mint](https://github.com/regolith-labs/ore-mint)
- [entropy](https://github.com/regolith-labs/entropy)
- [ore-stake](https://github.com/regolith-labs/ore-stake)
- [ore-lst](https://github.com/regolith-labs/ore-lst)
- [ore-burn](https://github.com/regolith-labs/ore-burn)
- [ore-boost](https://github.com/regolith-labs/ore-boost)
- [ore-boost-rebase-worker](https://github.com/regolith-labs/ore-boost-rebase-worker)
- [grams](https://github.com/regolith-labs/grams)

## 02-mining-clients-pools

- [ore-starter-app](https://github.com/regolith-labs/ore-starter-app)
- [ore-app](https://github.com/regolith-labs/ore-app)
- [ore-cli](https://github.com/regolith-labs/ore-cli)
- [ore-cli-legacy](https://github.com/regolith-labs/ore-cli-legacy)
- [ore-pool](https://github.com/regolith-labs/ore-pool)
- [ore-pool-private](https://github.com/regolith-labs/ore-pool-private)
- [drillx](https://github.com/regolith-labs/drillx)
- [verus-hash](https://github.com/regolith-labs/verus-hash)
- [verus-cli](https://github.com/regolith-labs/verus-cli)
- [ore-gpu](https://github.com/regolith-labs/ore-gpu)

## 03-solana-framework-wallets

- [steel](https://github.com/regolith-labs/steel)
- [steel-book](https://github.com/regolith-labs/steel-book)
- [solana-mobile](https://github.com/regolith-labs/solana-mobile)
- [dioxus-wallet-adapter](https://github.com/regolith-labs/dioxus-wallet-adapter)
- [wallet](https://github.com/regolith-labs/wallet)
- [solana-playground](https://github.com/regolith-labs/solana-playground)
- [agave](https://github.com/regolith-labs/agave)
- [haraka-bpf](https://github.com/regolith-labs/haraka-bpf)

## 04-trading-liquidity

- [jupiter-swap-api-client](https://github.com/regolith-labs/jupiter-swap-api-client)
- [jupiter-dca-sdk](https://github.com/regolith-labs/jupiter-dca-sdk)
- [meteora_damm_sdk](https://github.com/regolith-labs/meteora_damm_sdk)
- [meteora-dlmm-sdk](https://github.com/regolith-labs/meteora-dlmm-sdk)
- [meteora-pools-sdk](https://github.com/regolith-labs/meteora-pools-sdk)
- [meteora-vault-sdk](https://github.com/regolith-labs/meteora-vault-sdk)
- [kliquidity-sdk](https://github.com/regolith-labs/kliquidity-sdk)
- [protobook](https://github.com/regolith-labs/protobook)

## 05-app-infrastructure

- [dioxus](https://github.com/regolith-labs/dioxus)
- [wry](https://github.com/regolith-labs/wry)
- [dioxus-charts](https://github.com/regolith-labs/dioxus-charts)
- [geyser-stream](https://github.com/regolith-labs/geyser-stream)
- [helius-rust-sdk](https://github.com/regolith-labs/helius-rust-sdk)
- [cargo-packager](https://github.com/regolith-labs/cargo-packager)
- [oauth1-rs](https://github.com/regolith-labs/oauth1-rs)

See `docs/blueshift-optional.md` for separately scoped Blueshift projects. Upstream licenses and contributions remain with their owners. No bundled project is automatically safe for wallet spending or deploy operations.


## Extended source collections

- **Regolith Labs:** 42 repository entries in `manifest.json`.
- **HardhatChad:** 25 repository entries in `hardhatchad-manifest.json`.
- **Blueshift:** 102 repository entries in `blueshift-manifest.json`.

Total **169 repository references**, before deduplication of upstream/fork relationships. Identical names from different owners remain distinct source snapshots; the archive does not falsely combine their contents. These are manifests only until cloned.

### Obtain the source archive

Open **Actions → Archive categorized upstream sources → Run workflow**. Default selection clones all three collections, skipping three particularly large Blueshift toolchain/validator forks. Select collections individually as needed. Retrieve the generated workflow artifact `ORE-MINECRAFT-source-archive` after successful completion.

Alternatively run `python3 scripts/clone_and_pack.py --collections regolith hardhat blueshift` on a GitHub-connected machine. Use `--include-large` only with adequate disk/time capacity. Each clone is shallow, keeps upstream LICENSE files and records its checked-out SHA in `provenance.json`. No single binary combines these projects and no ORE financial operation is enabled by this archive.


## Community miners and related ecosystem sources

The fourth collection, `community-manifest.json`, contains **56** repositories: Bifrost-Technologies (41), Cissoko420 (12), and the individual repositories `tonyke-bot/ore-miner`, `0xrsydn/ore-miner`, and `f3n1b00t/ore-containers` (3). The named Bifrost/Cissoko miner repositories are already included in their respective account inventories and are not double counted.

**Total:** 225 source references across four manifests. These are source candidates, not an audited, integrated miner. **Security:** third-party miners/containers may execute untrusted commands or handle wallet secrets; inspect all scripts, dependencies, and licenses before running. Never inject mainnet private keys into imported tools. ORE v4 Deploy, Claim and Checkpoint remain disabled in the EdgeORE game until their canonical layouts and verification gates pass.

To archive just the community collection, run `python3 scripts/clone_and_pack.py --collections community`. The GitHub Actions workflow offers the same collection selector. Current workspace is a manifest/bootstrap; cloned sources are generated only when an archive run succeeds.
