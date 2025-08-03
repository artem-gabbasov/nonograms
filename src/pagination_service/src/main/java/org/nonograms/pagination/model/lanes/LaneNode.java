package org.nonograms.pagination.model.lanes;

/**
 * Common ancestor of {@link org.nonograms.pagination.model.lanes.LaneGroup} and
 * {@link org.nonograms.pagination.model.lanes.Lane} to implement the Composite pattern.
 */
public abstract sealed class LaneNode permits Lane, LaneGroup {

    /**
     * It's essentially a stub to be overridden.
      */
    protected int getActualSize() {
        return 1;
    }
}
